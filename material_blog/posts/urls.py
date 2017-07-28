from django.conf.urls import url

from posts.views import PostView, PostsByCat, Like

urlpatterns = [
    url(r'^post/(?P<post_id>[\d]+)/', PostView.as_view(), name="certain_post"),
    url(r'^like/', Like.as_view(), name="like"),
    url(r'^category/(?P<category_id>[\d]+)/', PostsByCat.as_view(), name="certain_category"),
]