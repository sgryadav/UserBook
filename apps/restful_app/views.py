from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from .models import *
from django.contrib import messages
from .forms import UploadFileForm



def loginregpage(request):
     return render(request, "restful_app/loginreg.html")

def login(request):
    log_username = request.POST['login_username']
    errors = Users.objects.log_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['username'] = Users.objects.get(username=log_username).username
        request.session['id'] = Users.objects.get(username=log_username).id
        #request.session['email'] = Users.objects.get(email=log_email).email
        return redirect("/usersindex")

def registration(request):
    errors = Users.objects.reg_validator(request.POST)
    hashedpw = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = Users.objects.create(username=request.POST['username'], email=request.POST['email'], pw=hashedpw)
        user.save()
        request.session['username'] = user.username
        request.session['id'] = user.id
        return redirect('/usersindex')


def usersindex(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, "restful_app/usertable.html", context)

def edituser(request, id):
    errors = Users.objects.edit_validator(request.POST)
    this_id = id
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        redirect_url = "/users/" + this_id + "/edit"
        return redirect(redirect_url)
    else:
        editeduser = Users.objects.get(id=id)
        editeduser.username = request.POST['edit_username']
        editeduser.email=request.POST['edit_email'] 
        editeduser.save()
        request.session['username'] = editeduser.username
    return redirect("/usersindex")


def showuser(request, id):
    context = {
        "user": Users.objects.get(id=id),
        "posts_of_user": Users.objects.get(id=id).postswall
    }
   # query = "SELECT * FROM messages ORDER BY created_at DESC"
	#messages = mysql.query_db(query)	

	#cmtquery = "SELECT * FROM comments JOIN users ON comments.user_id = users.id JOIN messages ON messages.id = comments.msg_id ORDER BY comments.created_at ASC"
	#comments = mysql.query_db(cmtquery)
    return render(request,"restful_app/usershow.html", context)

def rendereditpage(request,id):
    context = {
        "user": Users.objects.get(id=id)
    }
    return render(request, "restful_app/useredit.html", context)


def makepost(request,id):
    current_user = Users.objects.get(username=request.session['username'])
    userwall = Users.objects.get(id=id)
    post = Posts.objects.create(user=current_user, userwall=userwall, body=request.POST.get('msgbody', False))
    context = {
        "user": userwall,
        "posts_of_user": userwall.postswall.order_by("-created_at") 
    }
    return render(request,"restful_app/usershow.html", context)

def makecomment(request,id):
    current_user = Users.objects.get(username=request.session['username'])
    this_post = Posts.objects.get(id=id)
    the_user_wall = this_post.userwall
    comment = Comments.objects.create(user=current_user, post=Posts.objects.get(id=id), content=request.POST.get('cmtbody', False))
    context = {
        "user": the_user_wall,
        "posts_of_user": the_user_wall.postswall.order_by("-created_at") 
    }
    return render(request,"restful_app/usershow.html", context)


def removepost(request, id):
    this_post = Posts.objects.get(id=id)
    the_user_wall = this_post.userwall
    Posts.objects.get(id=id).comments.all().delete()
    this_post.delete()
    context = {
        "user": the_user_wall,
        "posts_of_user": the_user_wall.postswall.order_by("-created_at") 
    }
    return render(request,"restful_app/usershow.html", context)

def removecomment(request, id):
    the_user_wall = Comments.objects.get(id=id).post.userwall
    Comments.objects.get(id=id).delete()
    context = {
        "user": the_user_wall,
        "posts_of_user": the_user_wall.postswall.order_by("-created_at") 
    }
    return render(request,"restful_app/usershow.html", context)

def logoff(request):
    request.session['username'] = False
    request.session['id'] = False
    return render(request, "restful_app/loginreg.html")


