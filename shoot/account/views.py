from django.shortcuts import render, redirect
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)
from .forms import UserLoginForm, UserRegistrationForm




# Create your views here.

def LoginView(request):
	message='Enter your username & Password.'
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username = username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/player/")
		else:
			message='Username or Password is wrong..!!'
		return redirect("/accounts/login/")


	return render(request, 'login.html', {'form':form, 'message': message})


def Registration(request):
	print(request.user)
	form = UserRegistrationForm(request.POST or None)

	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password=password)
		login(request, new_user)
		return redirect("/player/")


	return render(request, 'registration_form.html', {'form':form})

def UserLogout(request):
	logout(request)
	return redirect("/accounts/login/")
