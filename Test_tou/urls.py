# Test_tou URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin,auth
from django.urls import path, include
from rest_framework import routers

from .controller import views,login,api
from myapp.models import User


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'123', api.UserViewSet)
router.register(r'456', api.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='home'),
    path('add_edition/', views.add_edition,name='add_edition'),
    path('my_favorite/', views.my_favorite,name='my_favorite'),
    path('other_favorite_page/', views.other_favorite_page,name='other_favorite_page'),
    path('other_favorite_ajax/', views.other_favorite_ajax,name='other_favorite_ajax'),
    path('change_edition/', views.change_edition,name='change_edition'),
    path('login/', login.login),
    path('logout/', login.logout,name='logout'),
    path('register/', login.register),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
