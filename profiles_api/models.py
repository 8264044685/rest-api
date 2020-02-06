from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# You can create your model here

class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, username, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError('Users must have a username')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Create and save a new sueperuser with given detail"""
        user = self.create_user(email, username, password)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser):
    """ Database model for user in the system """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserProfileManager()

    def __str__(self):
        """Return string representation of our user"""
        return self.email

    def has_perm(self, perm, obj=None):
        """For checking permissions. to keep it simple all admin have ALL permissons"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)"""
        return True
