from django.conf.urls import url

from posts.views import PostView, PostsByCat

urlpatterns = [
    url(r'^post/(?P<post_id>[\d]+)/', PostView.as_view(), name="certain_post"),
    url(r'^category/(?P<category_id>[\d]+)/', PostsByCat.as_view(), name="certain_category"),
]