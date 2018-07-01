from django import forms

from uploads.models import Document
from uploads.faceDetector import draw_face
from io import BytesIO
from PIL import Image
import base64
from django.core.exceptions import ValidationError
class DocumentForm(forms.Form):

    
    firstname = forms.CharField( max_length=255)
    lastname = forms.CharField( max_length=255)
    department = forms.CharField( max_length=255)
    employee_id = forms.IntegerField(required =False, widget=forms.HiddenInput())
    photo = forms.ImageField()

    def clean_photo(self):
        image_validator=1
        image = self.cleaned_data['photo']
        if type(image) is str:
            im = image.open(image)
        else: im= image

        face_no, image_drawn = draw_face(image.file.read())
        
        if face_no ==0:
            image_validator=0
        if face_no >1:
            image_validator=2

        return (image_validator, image, image_drawn)


        
       
       
