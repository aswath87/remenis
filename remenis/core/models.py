from django.db import models

class User(models.Model):
    fbid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=70)
    email = models.EmailField(blank=True, null=True)
    is_registered = models.BooleanField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Admin:
        pass

class Story(models.Model):
    authorid = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    story = models.TextField()
    story_date_year = models.IntegerField(blank=True, null=True)
    story_date_month = models.IntegerField(blank=True, null=True)
    story_date_day = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    is_private = models.BooleanField()
    
    class Admin:
        pass
    
class TaggedUser(models.Model):
    fbid = models.CharField(max_length=20)
    storyid = models.ForeignKey(Story)
        
    class Admin:
        pass

class StoryComment(models.Model):
    storyid = models.ForeignKey(Story)
    comment = models.TextField()
    post_date = models.DateTimeField(blank=True, null=True)
    
    class Admin:
        pass
    
class BetaEmail(models.Model):
    email = models.EmailField(blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    
    class Admin:
        pass