from __future__ import unicode_literals
from django.db import models
import re


NAME_REGEX = re.compile(r"(^[A-Z][-a-zA-Z]+$)")
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class Usermanager(models.Manager):

    def reg_validator(self, postData):
        errors = {}

        f_name = postData['f_name']
        l_name = postData['l_name']
        email = postData['email']

        if not NAME_REGEX.match(postData['f_name']):
           errors['first_name'] = "First name is invalid"
        if not NAME_REGEX.match(postData['l_name']):
           errors['last_name'] = "Last name is not valid"
        if not EMAIL_REGEX.match(postData['email']):
             errors['email'] = "Email is invalid"
        if Users.objects.filter(email=postData['email']):
             errors['email_exist'] = "Email has been used"
        return errors

    def edit_validator(self, postData):
        errors = {}
        f_name = postData['edit_fname']
        l_name = postData['edit_lname']
        email = postData['edit_email']

        if not NAME_REGEX.match(f_name):
            errors['first_name'] = "First name is invalid"
        if not NAME_REGEX.match(l_name):
            errors['last_name'] = "Last name is not valid"
        if not EMAIL_REGEX.match(email):
                errors['email'] = "Email is invalid"
        if Users.objects.filter(email=email):
                errors['email_exist'] = "Email has been used"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = Usermanager()


