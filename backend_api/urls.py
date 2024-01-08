from django.urls import include, path

urlpatterns = [
    path('', include('backend_api.api_v1.urls'),)
]