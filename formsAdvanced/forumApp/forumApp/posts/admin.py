from django.contrib import admin

from forumApp.posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'created_at', 'languages')
