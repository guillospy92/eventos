from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def logn(request, username, password):
	user = authenticate(username = username , password = password)
	if user is not None:
		if user.is_active:
			login(request, user)
		
		
		
	
	
		 
