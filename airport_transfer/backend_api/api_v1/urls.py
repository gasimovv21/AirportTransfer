from django.urls import include, path, re_path
from .views import CarViewSet, CarDetailView

from rest_framework.routers import DefaultRouter

routerv1 = DefaultRouter()
routerv1.register(r'cars', CarViewSet, basename='cars-list')

urlpatterns = [
    path('v1/', include(routerv1.urls)),
    re_path(r'v1/cars/(?P<id>\d+)/', CarDetailView.as_view(), name='car-detail'),
]
