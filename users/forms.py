from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.core import validators
def validete_username(value):
    if len(value)<=2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")

class CreateUser(UserCreationForm):
    password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={"placeholder":"Пароль",'autocomplete':'new-password','class':'form-control'}),error_messages={"required":"Please enter password"},)
    password2 = forms.CharField(label="Введіть пароль ще раз",widget= forms.PasswordInput(attrs={"placeholder":"Введіть пароль ще раз",'autocomplete':'new-password','class':'form-control'}),help_text="Переконайтеся, що ваш пароль містить малі літери, великі літери, цифри та символи",error_messages={"required":"Re-Enter password field cannot be empty"})
    username = forms.CharField(label="Ім'я користувача",widget=forms.TextInput(attrs={"placeholder":"Ім'я користувача","id":"username",'class':'form-control'}),validators=[validete_username])
    first_name = forms.CharField(label="Ім'я",widget=forms.TextInput(attrs={"placeholder":"Ім'я","required":True,'class':'form-control'}),error_messages={"required":"First name cannot be empty"})
    last_name = forms.CharField(label="Прізвище",widget=forms.TextInput(attrs={"placeholder":"Прізвище","required":True,'class':'form-control'}),error_messages={"required":"Last name cannot be empty"})
    email = forms.CharField(label="Пошта",widget=forms.EmailInput(attrs={"required":True,"Placeholder":"Пошта",'class':'form-control'}),error_messages={'required':'Email fields should not be empty'})
    class  Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']
    

class VerifyForm(forms.Form):
    otp = forms.CharField(label='OTP',max_length=70,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'OTP','required':True}),error_messages={'required':'Enter a otp'})


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Ім'я користувача",widget=forms.TextInput(attrs={"placeholder":"Ім'я користувача","class":"form-control"}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"placeholder":"Пароль",'autocomplete':'current-password',"class":"form-control"}))  