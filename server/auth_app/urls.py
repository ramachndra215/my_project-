from django.urls import path
from .views import RegisterUserView, UserProfileView # <-- Imports the RegisterUserView and UserProfileView

# Define the app namespace
app_name = 'auth_app'

urlpatterns = [
    # API endpoint that links React to the RegisterUserView
    path('register/', RegisterUserView.as_view(), name='register'),
     path('user/profile/', UserProfileView.as_view(), name='user-profile'),
]
