from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, UserProfileEditForm
from .models import Profile

# Task for decorator is to check if current user was authenticated
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': dashboard})

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance=request.user.profile,
                                           data=request.POST,
                                           files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.profile)

        return render(request, 'account/edit.html', {'user_form': user_form,
                                                     'profile_form': profile_form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Creating new user object, without saving in database
            new_user = user_form.save(commit=False)

            # Setting new password
            new_user.set_password(user_form.cleaned_data['password'])

            # Saving user object
            new_user.save()

            # Create user profile
            profile = Profile.objects.create(user=new_user)

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'account/register.html',
                  {'user_form': user_form})




# User login view
# def user_login(request):
#
#     if request.method == 'POST':
#
#         # Create form with sended user data
#         form = LoginForm(request.POST)
#
#         # Check if data in form is valid
#         if form.is_valid():
#             # Authenticate user based on data in database, get username and password and return user object or None
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 # Check if user is active
#                 if user.is_active:
#                     # Call login method and start session for user
#                     login(request, user)
#                     return HttpResponse('Uwierzytelnienie zakończone powodzeniem.')
#                 else:
#                     return HttpResponse('Konto zablokowane')
#             else:
#                 return HttpResponse('Podano nieprawidłowe dane')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

