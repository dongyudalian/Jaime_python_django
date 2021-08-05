from django.shortcuts import render,redirect
from django.contrib import auth
from myapp.models import User
from .loginForms import LoginForm
from django.core.exceptions import ValidationError

def login(request):
    
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    form = LoginForm(request.POST)
    
    name = request.POST.get('name')
    password = request.POST.get('password')
    User_info = auth.authenticate(username=name, password=password)
    print(name)
    print(password)
    print(User_info)
    if not User_info:
        form.add_error("password", " Your name and password didn't match. Please try again.")
        return render(request, 'login.html', {'form': form})
    else:
        auth.login(request, User_info)
        rep = redirect("/home/")
        rep.set_cookie("User_id", User_info.id)
        rep.set_cookie("User_name", User_info.username)
        rep.set_cookie("User_email", User_info.email)
        import datetime
        import time
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
        User_info.last_login = now
        User_info.save()
        return rep

def logout(request):
    auth.logout(request)
    rep = redirect("/home/")
    logout_successful = 1
    rep.set_cookie("logout_successful", logout_successful )
    return rep

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    email = request.POST.get('email')
    password = request.POST.get('password')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birthday')
    image = request.POST.get('image')
    import datetime
    import time
    created_time = datetime.datetime.now()
    created_time = created_time.strftime('%Y-%m-%d %H:%M:%S')
    created_time = datetime.datetime.strptime(created_time, '%Y-%m-%d %H:%M:%S')
    User.objects.create_user(email=email, password=password, username=name, gender=gender, birthday=birthday, image=image, created_time=created_time)

    rep = redirect("/home/")
    register_successful = 1
    rep.set_cookie("register_successful", register_successful )

    return rep