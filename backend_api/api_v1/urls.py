from django.urls import include, path, re_path
from .views import CarViewSet, CarDetailView, LocationView, AlbumView

from rest_framework.routers import DefaultRouter

routerv1 = DefaultRouter()
routerv1.register(r'cars', CarViewSet, basename='cars-list')
routerv1.register('locations', LocationView, basename='locations-list')
routerv1.register('album', AlbumView, basename='album-list')

urlpatterns = [
    path('v1/', include(routerv1.urls)),
    re_path(r'v1/cars/(?P<id>\d+)/', CarDetailView.as_view(), name='car-detail'),
]
