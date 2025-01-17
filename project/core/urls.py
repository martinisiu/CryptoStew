from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
#from rest_framework import routers

"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'entries', views.BitcoinEntrySerializer)
"""

urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders", include("orders.urls")),
    #path("api",include("Coin.urls"))
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
