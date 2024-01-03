from django.urls import include, path
from .views import CarViewSet, get_jwt_token, register

from rest_framework.routers import DefaultRouter

routerv1 = DefaultRouter()
routerv1.register('cars', CarViewSet, basename='cars-list')

auth_urls = [
    path('signup/', register, name='register'),
    path('token/', get_jwt_token, name='token')
]

urlpatterns = [
    path('v1/', include(routerv1.urls)),
    path('v1/auth/', include(auth_urls)),
]
