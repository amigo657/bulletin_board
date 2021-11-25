from django.shortcuts import render
from users.forms import UserLogIn, UserSignIn
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required


def signin(request):
    context = {"signin_form": UserSignIn()}
    if request.method == "POST":
        user_form = UserSignIn(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("log_in")
        context.update(signin_form = user_form)
    return render(request, "sign_in.html", context)

def login(request):
    context = {"login_form": UserLogIn()}
    if request.method == "POST":
        user_form = UserLogIn(request.POST)
        if user_form.is_valid():
            user_form.login(request)
            return redirect("home_page")
        context.update(login_form=user_form)
    return render(request, "log_in.html", context)

@login_required(login_url="log_in")
def logout(request):
    log_out(request)
    return redirect("home_page")