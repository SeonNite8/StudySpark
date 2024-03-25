from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html'

    
class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('homepage')
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)