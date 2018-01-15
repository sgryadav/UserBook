from django import forms
from .models import *

class UploadFileForm(forms.Form):
    class Meta:
        model = Users
        fields= (
            'f_name',
            'l_name',
            'email',
            'image' 
        )
        
  


