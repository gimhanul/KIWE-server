from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'birth', 'gender')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'birth', 'gender', 'is_active', 'is_admin', 'date_joined')

    def clean_password(self):
        return self.initial["password"]
 

'''
def signup(self, request, User):
    if(self.password==self.passwordcheck):
        User.id=self.cleaned_data['id']
        User.password=self.cleaned_data['password']
        User.birth=self.cleaned_data['birth']
        User.gender=self.cleaned_data['gender']
        User.phonenumber=self.cleaned_data['phonenumber']
        User.agree=self.cleaned_data['agree']
        User.save()
'''