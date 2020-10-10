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
