from django.shortcuts import render, reverse
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json

from posts.models import BlogPost, Category


class PostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(BlogPost, pk=post_id)
        post.views += 1
        post.save()
        return render(request, "singlepost.html", {"object": post})


class Like(View):
    def get(self, request):
        user = request.user
        post_id = request.GET.get('post_id', None)
        post = get_object_or_404(BlogPost, pk=post_id)

        if post.likes.filter(id=user.id).exists():
            # user has already liked this post
            # remove like/user
            post.likes.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a post
            post.likes.add(user)
            message = 'You liked this'

        ctx = {'likes_count': post.total_likes(), 'message': message}
        # use mimetype instead of content_type if django < 5
        return HttpResponse(json.dumps(ctx), content_type='application/json')


class PostsByCat(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        posts = BlogPost.objects.filter(category_id=category.id).order_by("-views")
        return render(request, "posts_by_cat.html", {"posts": posts, "category": category})