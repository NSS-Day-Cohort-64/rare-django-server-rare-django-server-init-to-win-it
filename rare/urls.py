from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rareapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]