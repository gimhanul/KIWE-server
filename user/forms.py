from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ('email', 'name', 'birth', 'gender')

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        else :
            user.set_password(password2)
            if commit:
                user.save()
            return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'birth', 'gender', 'is_active', 'is_admin', 'date_joined')

    def clean_password(self):
        return self.initial["password"]


class AuthenticationForm(forms.ModelForm):
    password  = forms.CharField()

    class Meta:
        model  =  User
        fields =  ('email', 'password')


class ImageUploadForm(forms.Form):
    profileImage = forms.ImageField()