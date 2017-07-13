from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404


from posts.models import BlogPost
# Create your views here.
class PostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(BlogPost, pk=post_id)
        return render(request, "singlepost.html", {"object": post})
