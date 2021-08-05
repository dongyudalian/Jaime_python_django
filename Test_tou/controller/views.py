from datetime import time, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    User_id = request.COOKIES.get('User_id')
    User_name = request.COOKIES.get('User_name')
    User_email = request.COOKIES.get('User_email')
    register_successful = request.COOKIES.get('register_successful')
    logout_successful = request.COOKIES.get('logout_successful')
    if not request.user.is_authenticated:
        rep = render(request, "home.html",{'register_successful':register_successful,'logout_successful':logout_successful})
        rep.delete_cookie("register_successful")
        rep.delete_cookie("logout_successful")
        return rep
    else:
        return render(request, "home.html",{'User_id':User_id,'User_name':User_name,'User_email':User_email})
