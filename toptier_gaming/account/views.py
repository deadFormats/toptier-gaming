from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse("Authenticated Successfully.")
            else:
                return HttpResponse("Invalid Credentials")
                
    else:
        form = LoginForm()
    return render(
        request,
        'account/login.html',
        {'form': form}
    )
