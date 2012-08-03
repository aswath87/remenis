from django.db import models

class User(models.Model):
    fbid = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    is_registered = models.BooleanField()
    last_date = models.DateTimeField(blank=True, null=True)
    page_views = models.IntegerField(default=0)

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
    page_views = models.IntegerField(default=0)
    fbid_for_migration = models.CharField(max_length=20, default="")
    
    class Admin:
        pass
    
class TaggedUser(models.Model):
    storyid = models.ForeignKey(Story)
    taggeduserid = models.ForeignKey(User, blank=True, null=True)
    fbid_for_migration = models.CharField(max_length=20, default="")
        
    class Admin:
        pass

class StoryComment(models.Model):
    storyid = models.ForeignKey(Story)
    authorid = models.ForeignKey(User, blank=True, null=True)
    comment = models.TextField()
    post_date = models.DateTimeField(blank=True, null=True)
    fbid_for_migration = models.CharField(max_length=20, default="")
    
    class Admin:
        pass

class StoryLike(models.Model):
    storyid = models.ForeignKey(Story)
    authorid = models.ForeignKey(User)
    fbid_for_migration = models.CharField(max_length=20, default="")
    
    class Admin:
        pass
        
class BetaEmail(models.Model):
    email = models.EmailField(blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    
    class Admin:
        pass