from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserRegistrationSerializer
from .models import Skill
class RegisterUserView(APIView):
    permission_classes = ()  # Allow any user (authenticated or not) to access this view

    def post(self, request):
        data = request.data.copy()

        # Convert skill names to Skill IDs
        skill_names = data.get('selected_skills', [])
        if isinstance(skill_names, list):
            skill_qs = Skill.objects.filter(name__in=skill_names)
            data['selected_skills'] = [skill.id for skill in skill_qs]

        serializer = CustomUserRegistrationSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully. Please proceed to login.',
                'username': user.username,
                'email': user.email,
            }, status=status.HTTP_201_CREATED)

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