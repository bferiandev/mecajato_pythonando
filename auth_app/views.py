from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class AuthAppLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('pages:dashboard')
    redirect_authenticated_user = True

    

