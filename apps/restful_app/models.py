from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
import re
import bcrypt


EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class Usermanager(models.Manager):

    def reg_validator(self, postData):
        errors = {}

        username = postData['username']
        email = postData['email']
        password = postData['pass']
        conf_password = postData['confirm_pass']

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is invalid"
        if Users.objects.filter(username=postData['username']):
            errors['username_exist'] = "Username has been used" 
        if Users.objects.filter(email=postData['email']):
            errors['email_exist'] = "Email has been used"
        if not PASS_REGEX.match(password):
            errors['pw1'] = "Password is invalid"
        if password != conf_password:
            errors['pw2'] = "Password does not match"
        return errors

    def log_validator(self, postData):
        errors = {}

        log_username = postData['login_username']
        log_pw = postData['login_pass']

        if Users.objects.filter(username=log_username).exists() == False:
            errors['not_username'] = "Invalid username"
        else:
            db_pw = Users.objects.get(username=log_username).pw
            if not bcrypt.checkpw(log_pw.encode(), db_pw.encode()):
                errors['not_match'] = "Invalid password"
        return errors

    def edit_validator(self, postData):
        errors = {}
        username = postData['edit_username']
        email = postData['edit_email']

        if not EMAIL_REGEX.match(email):
                errors['email'] = "Email is invalid"
        return errors

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Usermanager()

class Posts(models.Model):
    user = models.ForeignKey(Users, related_name = "posts")
    userwall = models.ForeignKey(Users, related_name="postswall")
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)


class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name="comments")
    user = models.ForeignKey(Users, related_name = "comments")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)



