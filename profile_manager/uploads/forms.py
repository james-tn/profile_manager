from django import forms

from uploads.models import Document
from uploads.faceDetector import draw_face
from io import BytesIO
from PIL import Image
import base64
from django.core.exceptions import ValidationError
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'employee_id','firstname','lastname', 'department','photo')
        labels = {
        "firstname": "First Name","lastname":"Last Name", "department":"Department", "photo": "Photo", "employee_id":"Employee ID"
    }

    def clean_photo(self):
        image_validator=1
        image = self.cleaned_data['photo']
        im = image.open(image)

        face_no, image_drawn = draw_face(image.file.read())



        
        if face_no ==0:
            image_validator=0
        if face_no >1:
            image_validator=2

        return (image_validator, image, image_drawn)


        
       
       
