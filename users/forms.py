from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.core import validators


def validete_username(value):
    if len(value)<=2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")

class CreateUser(UserCreationForm):
    password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={"placeholder":"Пароль",'autocomplete':'new-password','class':'form-control'}),error_messages={"required":"Будь ласка, введіть пароль"},)
    password2 = forms.CharField(label="Введіть пароль ще раз",widget= forms.PasswordInput(attrs={"placeholder":"Введіть пароль ще раз",'autocomplete':'new-password','class':'form-control'}),help_text="Переконайтеся, що ваш пароль містить малі літери, великі літери, цифри та символи",error_messages={"required":"Поле повторного введення пароля не може бути порожнім"})
    username = forms.CharField(label="Ім'я користувача",widget=forms.TextInput(attrs={"placeholder":"Ім'я користувача","id":"username",'class':'form-control'}),validators=[validete_username])
    first_name = forms.CharField(label="Ім'я",widget=forms.TextInput(attrs={"placeholder":"Ім'я","required":True,'class':'form-control'}),error_messages={"required":"Ім'я не може бути порожнім"})
    last_name = forms.CharField(label="Прізвище",widget=forms.TextInput(attrs={"placeholder":"Прізвище","required":True,'class':'form-control'}),error_messages={"required":"Прізвище не може бути порожнім"})
    email = forms.CharField(label="E-mail",widget=forms.EmailInput(attrs={"required":True,"Placeholder":"E-mail",'class':'form-control'}),error_messages={'required':'Поля електронної пошти не повинні бути порожніми'})
    class  Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']
    

class VerifyForm(forms.Form):
    otp = forms.CharField(label='Код',max_length=70,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Код','required':True}),error_messages={'required':'Введіть код'})


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Ім'я користувача",widget=forms.TextInput(attrs={"placeholder":"Ім'я користувача","class":"form-control"}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"placeholder":"Пароль",'autocomplete':'current-password',"class":"form-control"}))  