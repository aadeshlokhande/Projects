from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


# Create your views here.
def user_login(request):
    error = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # print(f"email = {email} and password = {password}")
        if len(username)==0:
            error['username_require_error'] = "Username Required"
        if len(password)==0:
            error['password_require_error'] = "Password Required"
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login successful")
            return redirect('dashboard_home')
        else:
            print("invalid credential")

    return render(request,"accounts/login.html",context={'error':error})

