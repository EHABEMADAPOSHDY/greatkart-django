from django import forms 
from .models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password' ,
        'class':'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password'
    }))
    class Meta:
        model = Account
        fields = ['first_name' , 'last_name' , 'phone_number' , 'email' , 'password']
    
    def __init__(self,*args,**kwargs):
        super(RegistrationForm , self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Numper'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
    def clean(self):
        cleaned_date = super(RegistrationForm , self).clean()
        password = cleaned_date.get('password')
        confirm_password = cleaned_date.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "Password dose not match!"
            ) 