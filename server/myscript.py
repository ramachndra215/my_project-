import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_skill_project.settings')
django.setup()

from auth_app.models import CustomUser

# Your code using CustomUser here
print(CustomUser.objects.all())