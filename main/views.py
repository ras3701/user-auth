from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from win10toast import ToastNotifier

# toaster = ToastNotifier()

# Create your views here.
def homepage(request):
    return render(request=request,
                    template_name="HomePage.html",
                    )

def loginpage(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,"You are logged in as {username}")
                return redirect("main:homepage")
        else:
            messages.error(request, f"Incorrect credentials! Please try again.")
	    return redirect("main:homepage")
    else:
        form = AuthenticationForm
        return render(request=request,
                    template_name="login-page.html",
                    context = {"form": form})


def signuppage(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Created New Account: {username}")
            login(request, user)
            messages.info(request, f"you are now logged in as {username}")
            return redirect("main:homepage")
        else:
            messages.error(request, f"Error Signing Up, Please try again")

    form = UserCreationForm
    return render(request=request,
                    template_name="SignUpPage.html",
                    context={"form": form})

def logoutpage(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("main:homepage")
