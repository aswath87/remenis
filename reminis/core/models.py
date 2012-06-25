from django.db import models

class User(models.Model):
    fbid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=70)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Story(models.Model):
    authorid = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    story = models.CharField(max_length=500)
    story_date = models.DateField(blank=True)

class TaggedUser(models.Model):
    fbid = models.CharField(max_length=20)
    storyid = models.ForeignKey(Story)