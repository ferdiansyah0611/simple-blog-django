from django.shortcuts import render, redirect
from django.contrib.auth import logout

def signout(request):
	logout(request)
	return redirect('/admin/login')