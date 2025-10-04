from django.db import models
from django.contrib.auth.models import AbstractUser

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# We extend the AbstractUser model to add extra fields specific to B.Tech students.
class CustomUser(AbstractUser):
    """
    Custom User model to store essential student details needed for the AI ecosystem.
    Inherits fields like username, password, email, first_name, last_name from AbstractUser.
    """
    
    # Required fields for registration (on the second page, as per your flow)
    institute_name = models.CharField(max_length=255, blank=True, null=True, 
                                      help_text="Name of the B.Tech or relevant institution.")
    
    # Professional Links (for initial data gathering)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, 
                                   help_text="Student's LinkedIn profile URL.")
    github_url = models.URLField(max_length=200, blank=True, null=True, 
                                 help_text="Student's GitHub profile URL.")
    
    # B.Tech Goal (e.g., Software Engineering, Data Scientist)
    career_goal = models.CharField(max_length=255, null=False, default="Undecided")

    selected_skills = models.ManyToManyField(Skill, blank=True)
    
    # Set this to use email instead of username for login (common in modern apps)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email or self.username
