from django import forms

class PassengerForm(forms.Form):
    nick = forms.CharField(min_length=2,max_length=20,strip=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control'}))
