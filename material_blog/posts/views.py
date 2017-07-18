from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from posts.models import BlogPost, Category


class PostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(BlogPost, pk=post_id)
        post.views +=1
        post.save()
        return render(request, "singlepost.html", {"object": post})


class PostsByCat(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        posts = BlogPost.objects.filter(category_id=category.id).order_by("-views")
        return render(request, "posts_by_cat.html", {"posts": posts, "category": category})