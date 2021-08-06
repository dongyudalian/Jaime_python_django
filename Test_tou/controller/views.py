from datetime import time, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from myapp.models import Special_edition,User

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

def add_edition(request):
    if request.method == 'GET':
        User_id = request.COOKIES.get('User_id')
        User_name = request.COOKIES.get('User_name')
        User_email = request.COOKIES.get('User_email')
        add_successful = request.COOKIES.get('add_successful')
        rep = render(request,"add_edition.html",{'User_id':User_id,'User_name':User_name,'User_email':User_email,'add_successful':add_successful})
        rep.delete_cookie("add_successful")
        return rep
    User_name     = request.COOKIES.get('User_name')
    edition_name = request.POST.get('edition_name')
    edition_info    = request.POST.get('edition_info')
    user_id            = request.POST.get('user_id')
    import datetime
    import time
    created_time = datetime.datetime.now()
    created_time = created_time.strftime('%Y-%m-%d %H:%M:%S')
    created_time = datetime.datetime.strptime(created_time, '%Y-%m-%d %H:%M:%S')
    user_info = User.objects.get(id = user_id)
    Special_edition.objects.create(Edname=edition_name,Edinfo=edition_info, created_time=created_time,user_id=user_info)

    rep = redirect("/add_edition/",{'User_name':User_name})
    add_successful = 1
    rep.set_cookie("add_successful", add_successful )
    return rep

def my_favorite(request):
    if request.method == 'GET':
        User_id = request.COOKIES.get('User_id')
        user_info = User.objects.get(id = User_id)
        ed_info = Special_edition.objects.filter(user_id =user_info)
        return render(request, "my_favorite.html",{'ed_info':ed_info})
    edition_id = request.POST.get('edition_id')
    Special_edition.objects.filter(id = edition_id).delete()
    rep = redirect("/my_favorite/")
    return rep