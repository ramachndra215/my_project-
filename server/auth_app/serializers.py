from rest_framework import serializers
from .models import CustomUser

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'password2',
            'first_name', 'last_name', 'institute_name',
            'linkedin_url', 'github_url', 'career_goal', 'selected_skills'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            institute_name=validated_data.get('institute_name', None),
            linkedin_url=validated_data.get('linkedin_url', None),
            github_url=validated_data.get('github_url', None),
            career_goal=validated_data.get('career_goal', None),
        )
        return user