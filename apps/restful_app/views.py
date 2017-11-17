from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def usersindex(request):
    context = {
        'users': Users.objects.all()
    }
    request.session['id'] = Users.objects.last().id
    return render(request, "restful_app/usertable.html", context)

def process(request): 
    errors = Users.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/users/create")
    else:
        user = Users.objects.create(first_name=request.POST['f_name'],last_name=request.POST['l_name'], email=request.POST["email"])

    return redirect("/users")

def edit(request, id):
    errors = Users.objects.edit_validator(request.POST)
    this_id = id
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        redirect_url = "/users/" + this_id + "/edit"
        return redirect(redirect_url)
    else:
        editeduser = Users.objects.get(id=id)
        editeduser.first_name=request.POST['edit_fname']
        editeduser.last_name=request.POST['edit_lname']
        editeduser.email=request.POST['edit_email']
        editeduser.save()
    return redirect("/users")

def newuser(request):
    return render(request,"restful_app/usercreate.html")

def showuser(request,id):
    context = {
        "user": Users.objects.get(id=id)
    }
    return render(request,"restful_app/usershow.html", context)

def edituser(request,id):
    context = {
        "user": Users.objects.get(id=id)
    }
    return render(request, "restful_app/useredit.html", context)

def deleteuser(request,id):
    b = Users.objects.get(id=id)
    b.delete()
    return redirect("/users")


