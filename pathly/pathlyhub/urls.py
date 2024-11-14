from django.urls import path
from .views import RegisterView, LoginView, ProfileCreateView, ProfileUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/create/', ProfileCreateView.as_view(), name='create_profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='update_profile'),
]
