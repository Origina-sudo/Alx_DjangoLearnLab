from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserRegistrationSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserRegistrationSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key
            })
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

#follows the user with a specific user_id
@api_view(['POST'])
def follow_user(request, user_id):
    permissions.IsAuthenticated
    user_to_follow = get_objects_or_404(CustomUser, id=user_id)
    if request.user != user_to_follow:
        request.user.following.add(user_to_follow)
        return Response({'status': 'now following'}, status=status.HTTP_200_OK)
    return Response({'status': 'cannot follow self'}, status=status.HTTP_400_BAD_REQUEST)


@api_view
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
    request.user.following.remove(user_to_follow)
    return Response({'status': 'unfolloed'}, status=status.HTTP_200_OK)