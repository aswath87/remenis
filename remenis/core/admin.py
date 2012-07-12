from django.contrib import admin
from models import User, Story, TaggedUser, StoryComment

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name', 'email')
    search_fields = ('first_name', 'last_name', 'full_name', 'email')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'authorid', 'title', 'story', 'story_date_year', 'story_date_month', 'story_date_day', 'post_date')
    list_filter = ('authorid',)
    date_hierarchy = 'post_date'
    ordering = ('-post_date',)
    raw_id_fields = ('authorid',)

class TaggedUserAdmin(admin.ModelAdmin):
    list_display = ('fbid', 'storyid')
    search_fields = ('fbid', 'storyid')
    
admin.site.register(TaggedUser, TaggedUserAdmin)
admin.site.register(StoryComment)
admin.site.register(User, UserAdmin)
admin.site.register(Story, StoryAdmin)