from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings



class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        
        email=self.normalize_email(email)
        user = self.model(email=email , name=name)


        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,name,password):
        """Create and save a new user name with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser =True
        user.is_staff =True
        user.save(using=self._db)

        return user


        
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for User"""
    email = models.EmailField(max_length=290 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']

    def get_full_name(self):
        """Retrieve Full name of user"""
        return self.name

    def short_name(self):
        """Retrieve short name"""
        return self.name

    def __str__(self):
        """Returning string representation of our user"""
        return self.email



class ProfileFeedItem(models.Model):
    """Profile status updated"""
    user_profile = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       on_delete = models.CASCADE, 
    )
status_text = models.CharField(max_length=400)
created_on = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """Return the model as the string"""
    return self.status_text