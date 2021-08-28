from django import forms

class SignupForm(forms.Form):
    id=forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    passwordcheck = forms.CharField(max_length=10)
    birth = forms.DateField()
    gender = forms.CharField(max_length=1) #m=man, w=woman
    phonenumber = forms.CharField(max_length=10)
    agree = forms.IntegerField()

    def signup(self, request, User):
        if(self.password==self.passwordcheck):
            User.id=self.cleaned_data['id']
            User.password=self.cleaned_data['password']
            User.birth=self.cleaned_data['birth']
            User.gender=self.cleaned_data['gender']
            User.phonenumber=self.cleaned_data['phonenumber']
            User.agree=self.cleaned_data['agree']
            User.save()

