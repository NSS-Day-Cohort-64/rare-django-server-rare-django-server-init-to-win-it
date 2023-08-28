from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rareapi.views import register_user, login_user
from rest_framework import routers
from rareapi.views import CategoryView, PostView, CommentView, TagView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')
router.register(r'posts', PostView, 'post')
router.register(r'comments', CommentView, 'comment')
router.register(r'tags', TagView, 'tag')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]