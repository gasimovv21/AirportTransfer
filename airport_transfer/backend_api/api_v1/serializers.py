from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from cars.models import Car, Feature
from users.models import User
from rest_framework.validators import UniqueValidator


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


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name')
        model = User


class RegisterDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError('Using username "me" is denied')
        return value

    class Meta:
        fields = ('username', 'email')
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
