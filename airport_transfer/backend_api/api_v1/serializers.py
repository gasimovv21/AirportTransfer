from rest_framework import serializers
from cars.models import Car, Feature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['name']

class CarSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'category', 'price', 'availability_date', 'features', 'image']

    def get_features(self, obj):
        return [feature['name'] for feature in FeatureSerializer(obj.features.all(), many=True).data]
