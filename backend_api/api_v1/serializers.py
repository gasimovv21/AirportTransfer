from django.conf import settings
from rest_framework import serializers
from cars.models import Feature, Photo, Car, Location


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ['name', 'icon']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']

    def to_representation(self, instance):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(instance.image.url)
        else:
            # Если request отсутствует в контексте, используйте настройки Django
            return settings.MEDIA_URL + instance.image.url


class CarSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)
    photo_album = PhotoSerializer(many=True)

    class Meta:
        model = Car
        fields = ['id', 'name', 'category', 'price', 'availability_date', 'features', 'image', 'photo_album']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']

    def to_representation(self, instance):
        return instance.name
