from django.contrib.auth.models import User
from django.db import models


class UserProfileInfo(models.Model):
    ''' User model '''

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    portfolio_page = models.URLField(blank=True)
    portfolio_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
