from .services.user_services import (
    main_login_function,
)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def special(request):
    """ If User is already logged in
    redirect to already_logged_in page """

    return render(request, 'already_logged_in.html')

def user_login(request):
    """ User login Controller """

    if request.user.is_authenticated:
        return special(request)

    else:
        if request.method == "POST":
            return func(request)

        else:
            return render(request, 'login.html')

@login_required
def user_logout(request):
    """ Telling to User that he is
    logged in """

    logout(request)

    return HttpResponseRedirect('/')


def registration(request):
    """ Registration controller """

    if request.user.is_authenticated:
        return special(request)

    else:
        registered = False

        context = func(request, registered)

        return render(request, "registration.html", context)
