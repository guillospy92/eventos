from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegisterForm, LoginForm
from .models import  User
from .functions import logn




def userlogin(request):

	if request.method == "POST":
		if 'register-form' in request.POST:
				user_register = UserRegisterForm(request.POST)
				if user_register.is_valid():
					User.objects.create_user(username = user_register.cleaned_data['username'] , email = user_register.cleaned_data['email'], password = user_register.cleaned_data['password'])
					logn(request, user_register.cleaned_data['username'],user_register.cleaned_data['password'])
					
					return redirect ('/')

		if 'login-form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				logn(request, login_form.cleaned_data['username'],login_form.cleaned_data['password'])
				return redirect ('/')
				
				

	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
		return render (request, 'reguser.html', {'user_register':user_register, 'login_form':login_form})




def Logout(request):
	logout(request)
	return redirect('/')

 







