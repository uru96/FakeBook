from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Task for decorator is to check if current user was authenticated
#
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': dashboard})

# User login view
def user_login(request):

    if request.method == 'POST':

        # Create form with sended user data
        form = LoginForm(request.POST)

        # Check if data in form is valid
        if form.is_valid():
            # Authenticate user based on data in database, get username and password and return user object or None
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                # Check if user is active
                if user.is_active:
                    # Call login method and start session for user
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończone powodzeniem.')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Podano nieprawidłowe dane')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

