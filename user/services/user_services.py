from django.contrib.auth import (
    authenticate,
    login,
)
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render


def login_process(request, user, username):
    """ Check if User account is active and
    after login will be redirected to main page """

    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")

        else:
            return HttpResponse("Your account was inactive")

    else:
        print("Logging process was failed")
        print("Was used username: {}".format(username))
        return render(request, "login_error.html")

def main_login_function(request):
    """ Get username & password and take
    it into "login_process" """

    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username = username, password = password)

    login_response = login_process(request, user, username)

    return login_response

def save_new_user():
    """ Save info about User as new account """

    user = user_form.save()
    user.set_password(user.password)
    user.save()

    profile = profile_form.save(commit=False)
    profile.user = user

    if 'portfolio_img' in request.FILES:
        print('YEAH')
        profile.portfolio_picture = request.FILES['portfolio_img']

    profile.save()
    registered = True
    return registered

def main_registration_func(request):
    """ Get registration info from User
    and take it into 'save_new_user' function """

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            save_new_user()

        else:
            print(user_form.errors, profile_form.errors)
            return HttpResponse(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }

    return context
