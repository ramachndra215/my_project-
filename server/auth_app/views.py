from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserRegistrationSerializer

class RegisterUserView(APIView):
    permission_classes = ()  # Allow any user (authenticated or not) to access this view

    def post(self, request):
        print(request.data)
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully. Please proceed to login.',
                'username': user.username,
                'email': user.email,
            }, status=status.HTTP_201_CREATED)
        
        # 🔥 This handles the invalid case
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "username": user.username,
            "career_goal": getattr(user, "career_goal", ""),
            "selected_skills": [skill.name for skill in getattr(user, "selected_skills", []).all()] if hasattr(user, "selected_skills") else [],
        }
        return Response(data)