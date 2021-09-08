from django import forms

class OnceDataForm(forms.form):
    where = forms.IntegerField()
    when = forms.IntegerField()
    who = forms.IntegerField()
    