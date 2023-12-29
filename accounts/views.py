from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        phone_number = form.cleaned_data["phone_number"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        username = email.split("@")[0]
        user = Account.objects.create_user(
            first_name, last_name, username, email, password
        )
        # Since we do not have a phone number field in the model so we create a new field after creating the object
        user.phone_number = phone_number
        user.save()
        messages.success(request, "Registration Successful")
    else:
        pass

    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, "Login success!")
            return redirect("home")
        else:
            messages.error(request, "Invaild credentials!")
            return redirect("login")
    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out!")
    return redirect("login")


def dashboard(request):
    pass
