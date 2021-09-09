from django import forms

class OnceDataForm(forms.form):
    where = forms.CharField()
    howmany = forms.CharField()
    what = forms.CharField()
    relationship = forms.CharField()
    