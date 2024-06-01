# django forms

from django import forms
class userforms(forms.Form):
    name=forms.CharField(label='name',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    # use boostrap class form control
    email=forms.CharField(label='email',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    passoword=forms.CharField(label='password',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

   