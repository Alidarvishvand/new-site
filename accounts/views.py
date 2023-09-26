from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            form = LoginForm()
            return render(request,'accounts/login.html', {'form': form})
        
        elif request.method == 'POST':
            form = LoginForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request, user)
                    messages.success(request,f'Hi {username.title()}, welcome back!')
                    return redirect('/')
            
            # form is not valid or user is not authenticated
            messages.error(request,f'Invalid username or password')
            return render(request,'accounts/login.html',{'form': form})
        
    else:
        return redirect('/')
            



    # if request.user.is_authenticated:
    #     msg = 'user is authenticated'
    # else:
    #     msg = 'user is not authenticated'
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')




def signup_view(request):
    print("hello")
    return render(request, 'accounts/signup.html')