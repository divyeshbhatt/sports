from django import forms
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

	


class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name'}))
	email 	 = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
	email2 	 = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Confirm Email'}))
	password 	 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	class Meta:
		model = User
		fields = ('username', 'email','email2', 'password')

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')

		if email != email2:
			raise forms.ValidationError('Emails Not Match..')
		email_qs = User.objects.filter(email = email)
		if email_qs.exists():
			raise forms.ValidationError('Email already exists..!')
		return email2


	
