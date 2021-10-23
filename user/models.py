from django.db import models
from django.db.models.expressions import F
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, birth, gender, password=None):
        if not email:
            raise ValueError('Please enter your email')
        
        user = self.model(
            email = UserManager.normalize_email(email),
            birth = birth,
            gender = gender,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birth, gender, password):
        user = self.create_user(
            email=self.normalize_email(email),
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
    birth=models.DateField()
    gender = models.SmallIntegerField()
    friends = models.ManyToManyField('User', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth', 'gender']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.is_admin

class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150, default='')
    image = models.ImageField(upload_to='Profile/', blank=True, default='Profile/default.png')
    is_kiwe = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


#friends
class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE)


#notification
class Notification(models.Model):

    TYPE_CHOICES = (
        ('request', 'Request'),
        ('accept', 'Accept'),
    )

    to_user = models.ForeignKey(
        User, related_name='noti_to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        User, related_name='noti_from_user', on_delete=models.CASCADE)
    notitype = models.CharField(max_length=20, choices=TYPE_CHOICES)
    notidatetime = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)
    requestID = models.ForeignKey(FriendRequest, null=True, on_delete=models.SET_NULL)