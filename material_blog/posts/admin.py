from django.contrib import admin
from posts.models import Category, InterestTag, BlogPost, BlogPostComment


class BlogpostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "email", "post")

admin.site.register(Category)
admin.site.register(InterestTag)
admin.site.register(BlogPost, BlogpostAdmin)
admin.site.register(BlogPostComment, CommentAdmin)
