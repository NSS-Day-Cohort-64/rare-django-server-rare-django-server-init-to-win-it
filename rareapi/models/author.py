from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @property
    def email(self):
        return f'{self.user.email}'
    
    @property
    def username(self):
        return f'{self.user.username}'
    
    @property
    def date_joined(self):
        return f'{self.user.date_joined}'
    
    @property
    def is_staff(self):
        return f'{self.user.is_staff}'
    