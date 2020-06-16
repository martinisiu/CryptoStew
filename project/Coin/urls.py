from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from Coin import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename="Users")
router.register(r'groups', views.GroupViewSet, basename="Groups")
router.register(r'entries', views.BitcoinEntrySerializer, basename="Bitcoin Entries")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]