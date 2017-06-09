from django.shortcuts import render
from django.views import View

from posts.models import BlogPost, Category
from users.models import User


class HomeView(View):
    def get(self, request):
        posts = BlogPost.objects.filter(author_id=request.user.id)
        amount = len(posts)
        categories = Category.objects.all()
        return render(request, 'home.html', {'posts': posts[:10], 'amount': amount, 'categories': categories})