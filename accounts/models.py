from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20, blank=True)
    avatar = models.URLField(blank=True, max_length=500, null=True)  # store URL to Supabase file

    def __str__(self):
        return self.user.username
