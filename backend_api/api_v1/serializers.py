from rest_framework import serializers
from cars.models import Feature, Photo, Car


class FeatureSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Feature
        fields = ['name', 'icon']
    

    def get_icon(self, obj):
        return obj.icon.url if obj.icon else None


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']


class CarSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Car
        fields = ['id', 'name', 'category', 'price', 'availability_date', 'features', 'image', 'photo_album']

    def get_photo_album(self, obj):
        return [photo['image'] for photo in PhotoSerializer(obj.photo_album.all(), many=True).data]