from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, name, email, birth, gender, password=None):
        if not email:
            raise ValueError('Please enter your email')
        
        user = self.model(
            email = UserManager.normalize_email(email),
            name = name,
            birth = birth,
            gender = gender,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, birth, gender, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name = name,
            birth = birth,
            gender = gender,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.CharField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20)
    birth=models.DateField()
    gender = models.SmallIntegerField()
    friends = models.ManyToManyField('User', related_name='friend', black=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birth', 'gender']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.is_admin


#friends
class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE)