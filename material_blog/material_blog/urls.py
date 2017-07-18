"""material_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from core.views import HomeView
from posts.views import PostView, PostsByCat

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^home/', HomeView.as_view(), name="home"),
    url(r'^post/(?P<post_id>[\d]+)/', PostView.as_view(), name="certain_post"),
    url(r'^category/(?P<category_id>[\d]+)/', PostsByCat.as_view(), name="certain_category"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

