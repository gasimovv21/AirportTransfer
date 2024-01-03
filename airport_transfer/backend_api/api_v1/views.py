from rest_framework import viewsets
from rest_framework.response import Response
from cars.models import Car
from users.models import User
from .serializers import CarSerializer, RegisterDataSerializer, TokenSerializer

from rest_framework import permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from django.shortcuts import get_object_or_404

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import AccessToken


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = RegisterDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='AirportTransfer registration',
        message=f'Your confirmation code: {confirmation_code}',
        from_email=None,
        recipient_list=[user.email],
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )

    if default_token_generator.check_token(
            user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)},
                        status=status.HTTP_200_OK)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)