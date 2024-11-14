from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserProfileSerializer, ProfileSerializer
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

class ProfileCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user  # Obtain the authenticated User instance

        # Ensure the user is an actual User instance
        if not isinstance(user, User):
            raise ValueError("Authenticated user is not an instance of the User model.")

        # Check if the profile already exists to avoid duplication
        if Profile.objects.filter(user=user).exists():
            raise ValidationError("A profile for this user already exists.")

        # Save the profile with the user instance associated
        serializer.save(user=user)




class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
