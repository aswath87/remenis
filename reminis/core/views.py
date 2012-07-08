from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
import datetime, random, re, logging
from reminis.core.models import User, Story, TaggedUser
from reminis import settings

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

import urllib, urllib2, json

@csrf_exempt
def splash(request):
    return render_to_response('splash.html', locals())
    
@csrf_exempt
def login(request):
    debug = settings.DEBUG
    if 'token' in request.session:
        return redirect('/home/')
    else:
        return render_to_response('login.html', locals())

def logout(request):
    request.session.pop('token', None)
    request.session.pop('profile', None)
    request.session.pop('accessCredentials', None)
    return redirect('/')

@csrf_exempt
def home(request):
    active_tab = "home"

    if 'token' in request.session:
        fullname = getMyFullName(request)
        userid = (request.session['accessCredentials']).get('uid')
        photourl = (request.session['profile']).get('photo')
        return render_to_response('home.html', locals())
    elif 'token' in request.POST and request.POST['token']:
        request.session['token'] = request.POST['token']
        
        auth_info = getAuthInfo(request)
        if auth_info <> False:
            profile = auth_info['profile']
            request.session['profile'] = profile
            
            fullname = profile.get('displayName')
            photourl = profile.get('photo')
            email = profile.get('verifiedEmail')
            name = profile['name']
            firstname = name.get('givenName')
            lastname = name.get('familyName')
            
            request.session['accessCredentials'] = auth_info['accessCredentials']
            
            userid = (request.session['accessCredentials']).get('uid')
            
            try:
                user = User.objects.get(fbid=userid)
            except User.DoesNotExist:
                # save new user to user DB
                user_to_save = User(fbid=userid,
                                    first_name=firstname,
                                    last_name=lastname,
                                    full_name=fullname,
                                    email=email
                                    )
                user_to_save.save()
            
            return render_to_response('home.html', locals())
        else:
            return redirect('/')
    else:
        return redirect('/')

@csrf_exempt
def post(request): 
    errors = []
    debug = settings.DEBUG
    active_tab = "post"
    
    fullname = getMyFullName(request)
    userid = (request.session['accessCredentials']).get('uid')
    
    myfriends = getGraphForMe(request, 'friends', True)
    
    friends_name_array = [x['name'].encode('ASCII', 'ignore') for x in myfriends]
    friends_name_array.append(str(fullname))
    friends_name_array_temp = [str.replace(name, "'", "&#39;") if "'" in name else name for name in friends_name_array]
    friends_name_array_string =  str.replace(str(friends_name_array_temp), "'", "\"")
    
    friends_id_array = [x['id'].encode('ASCII', 'ignore') for x in myfriends]
    friends_id_array.append(str(userid))
    
    friends_dictionary = json.dumps(dict(zip(friends_id_array, friends_name_array)))
    
### HANDLE DUPLICATE NAMES 
#    import collections
#    friends_name_array_counter = collections.Counter(friends_name_array)
#    friends_name_array_duplicate = [i for i in y if y[i] > 1]
#    for duplicate_name in friends_name_array_duplicate:
#        for name in friends_name_array:
    
    if request.method == 'GET':
        return render_to_response('post.html', 
                                      locals(),
                                      RequestContext(request)
                                      )
    elif request.method == 'POST':
        user = User.objects.get(fbid=(request.session['accessCredentials']).get('uid'))
        
        date_month_int = 0
        if 'story_date_month' in request.POST:
            date_month_string = request.POST["story_date_month"]
            if date_month_string == "Jan":
                date_month_int = 1
            elif date_month_string == "Feb":
                date_month_int = 2
            elif date_month_string == "Mar":
                date_month_int = 3
            elif date_month_string == "Apr":
                date_month_int = 4
            elif date_month_string == "May":
                date_month_int = 5
            elif date_month_string == "Jun":
                date_month_int = 6
            elif date_month_string == "Jul":
                date_month_int = 7
            elif date_month_string == "Aug":
                date_month_int = 8
            elif date_month_string == "Sep":
                date_month_int = 9
            elif date_month_string == "Oct":
                date_month_int = 10
            elif date_month_string == "Nov":
                date_month_int = 11
            elif date_month_string == "Dec":
                date_month_int = 12
            
        date_day_int = 0
        if 'story_date_day' in request.POST:
            if request.POST["story_date_day"] != "---":
                date_day_int = request.POST["story_date_day"]
            
        story_to_save = Story(authorid=user,
                      title=request.POST["title"],
                      story=request.POST["story"],
                      story_date_year=request.POST["story_date_year"],
                      story_date_month=date_month_int,
                      story_date_day=date_day_int,
                      post_date=datetime.datetime.now()
                       )
        
        tagged_friends = (request.POST["tagged_friends"]).split(",")
        
        story_to_save.save()
        
        for tagged_friend in tagged_friends:
            taggedUser_to_save = TaggedUser(fbid=tagged_friend,
                                            storyid=story_to_save
                                            )
            taggedUser_to_save.save()
        
        active_tab = "search"
        return redirect('/search/?q=' + user.fbid)

@csrf_exempt
def search(request):
    active_tab = "search"
    
    fullname = getMyFullName(request)
    userid = (request.session['accessCredentials']).get('uid')
    
    if 'q' in request.GET:
        if request.GET['q']:
            query = request.GET['q']
            try:
                user = User.objects.get(fbid=query)
            except User.DoesNotExist:
                search_authorname = getUserFullName(request, query)
                error = 'A user with that authorid doesn\'t exist in Remenis.  Would you like to invite them to join Reminis?'
            else:
                stories_about_user = [x.storyid for x in TaggedUser.objects.filter(fbid = user.fbid)]
                stories_about_user_ids = [x.id for x in stories_about_user]
                tagged_users = []
                for story in stories_about_user:
                    tagged_users_in_story = TaggedUser.objects.filter(storyid = story)
                    tagged_users.append([int(x.fbid) for x in tagged_users_in_story])
                stories_dictionary = dict(zip(stories_about_user_ids, tagged_users))
                    
                stories_written_by_user = Story.objects.filter(authorid = user)
                search_authorname = user.full_name
            
            return render_to_response('search_results.html', locals())
        else:
            error = 'Please submit a search term.'
            return render_to_response('search_form.html', locals())
    else:
        return render_to_response('search_form.html', locals())


## UTILS

def getAuthInfo(request):
    api_params = {
        'token': request.session['token'],
        'apiKey': '5ab3ff51bb1b219c07e950e4d8b4dc1ad94496ad',
        'format': 'json',
    }
    # make the api call
    http_response = urllib2.urlopen('https://rpxnow.com/api/v2/auth_info', urllib.urlencode(api_params))
    
    # read the json response
    auth_info_json = http_response.read()
    
    # process the json response
    auth_info = json.loads(auth_info_json)

    if auth_info['stat'] == 'ok':
        return auth_info
    else:
        return False

def getGraphData(request, url_to_open):
    http_response = urllib2.urlopen(url_to_open)
    graph_json = http_response.read()
    graph = json.loads(graph_json)
    return graph['data']

def getGraphForMe(request, graph_string, access_token_needed=False):
    url_to_open = 'https://graph.facebook.com/' + (request.session['accessCredentials']).get('uid') + '/' + graph_string
    if access_token_needed:
        url_to_open += '?access_token=' + (request.session['accessCredentials']).get('accessToken')
    return getGraphData(request, url_to_open)

def getGraphCustom(request, graph_string, access_token_needed=False):
    url_to_open = 'https://graph.facebook.com/' + graph_string
    if access_token_needed:
        url_to_open += '?access_token=' + (request.session['accessCredentials']).get('accessToken')
    return getGraphData(request, url_to_open)

def getUserFullName(request, fbid):
    url_to_open = 'https://graph.facebook.com/' + fbid
    http_response = urllib2.urlopen(url_to_open)
    graph_json = http_response.read()
    graph = json.loads(graph_json)
    return graph['name']
    
def getMyFullName(request):
    user = User.objects.get(fbid=(request.session['accessCredentials']).get('uid'))
    return user.full_name
