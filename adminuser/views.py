from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User,AdminModel,App,Image

# Create your views here.
def index(request):
    return render(request, "adminuser/index.html")

def loginadmin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        admindata = AdminModel.objects.get(username=username)
        if admindata.password != password:
            return render(request,"adminuser/loginadmin.html",{
                "message":"Incorrect password"
            })
        return render(request,"adminuser/homeadmin.html")
    else:
        return render(request,"adminuser/loginadmin.html")

def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        userdata = User.objects.get(username=username)
        appdata = App.objects.all()
        if userdata.password != password:
            return render(request,"adminuser/loginuser.html",{
                "message":"Incorrect password"
            })
        return render(request,"adminuser/homeuser.html",{
            "user":userdata,
            "appdata":appdata
        })
    else:
        return render(request,"adminuser/loginuser.html")

def info(request,id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        print(user)
        return render(request,"adminuser/info.html",{
            "user":user
        })
    else:
        return render(request,"adminuser/homeuser.html")

def mapuserapp(request):
    if request.method == "POST":
        app = request.POST["app"]
        username = request.POST["username"]

        appdata = App.objects.get(app=app)
        userdata = User.objects.get(username=username)

        userdata.apps.add(appdata)
        return render(request, "adminuser/homeadmin.html",{
            "message":"User Mapped with App"
        })
    else:
        return render(request, "adminuser/homeadmin.html")

def appuser(request,id):
    if request.method == "POST":
        appcategory = request.POST["appcategory"]
        image_link = request.POST.get("image")
        image = Image.objects.create(url=image_link)
        appinfo = appcategory.split()
        appname = appinfo[0]
        appdata = App.objects.get(app=appname)
        allapps = App.objects.all()
        userdata = User.objects.get(pk=id)

        userdata.apps.add(appdata)
        userdata.image = image
        userdata.save()
        return render(request,"adminuser/homeuser.html",{
            "message":"App added to your list",
            "appdata":allapps
        })
    else:
        return render(request, "adminuser/homeuser.html")

def homeuser(request):
    appdata = App.objects.all()
    return render(request,"adminuser/homeuser.html",{
        "appdata":appdata
    })

def addapp(request):
    if request.method == "POST":
        app = request.POST["app"]
        points = request.POST["points"]

        appData = App(app=app,points=points)
        appData.save()
        return render(request, "adminuser/homeadmin.html", {
            "message": "App added"
        })

def homeadmin(request):
    return render(request,"adminuser/homeadmin.html")

def registeradmin(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        role = request.POST["role"]
        if password != confirmation:
            return render(request, "adminuser/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = AdminModel(username=username,email=email,password=password,role=role)
            user.save()
        except IntegrityError:
            return render(request, "adminuser/register.html", {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse("homeadmin"))
    else:
        return render(request, "adminuser/registeradmin.html")

def registeruser(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        role = request.POST["role"]
        if password != confirmation:
            return render(request, "adminuser/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User(username=username,email=email,password=password,role=role)
            user.save()
        except IntegrityError:
            return render(request, "adminuser/register.html", {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse("homeuser"))
    else:
        return render(request, "adminuser/registeruser.html")
