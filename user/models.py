from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self,**kwargs):
        if not "email" in kwargs:
            raise ValueError('Please enter your email')
        
        user = self.model(
            email = UserManager.normalize_email(kwargs.get("email")),
        )
        user.set_password(self.normalize_email(kwargs.get("paassword")))
        user.save(using=self.db)
        return user

    def create_superuser(self, **kwargs):
        new_superuser = self.create_user(**kwargs)
        new_superuser.is_admin = True
        new_superuser.save(using=self._db)
        return new_superuser
'''
GENDER_CHOICES = (
    (0, 'Female')
    (1, 'Male')
    (2, 'Not to disclose')
)
'''

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    birth=models.DateField()
    gender = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.is_admin

'''
class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True) 
    password = models.CharField(max_length=10)
    agree = models.IntegerField()
    gender = models.CharField(max_length=1) #m=man, w=woman
    birth = models.DateField()
    phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return self.id
'''
'''
class Keyword(models.Model):
    keyword = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)

class'''