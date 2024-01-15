from rest_framework import serializers
from cars.models import Feature, Photo, Car


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['name', 'icon']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']


class CarSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    photo_album = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'category', 'price', 'availability_date', 'features', 'image', 'photo_album']

    def get_features(self, obj):
        return [feature['name'] for feature in FeatureSerializer(obj.features.all(), many=True).data]

    def get_photo_album(self, obj):
        return [photo['image'] for photo in PhotoSerializer(obj.photo_album.all(), many=True).data]