from django import forms

from uploads.models import Document
from uploads.faceDetector import draw_face
from io import BytesIO
from PIL import Image
import base64

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'employee_id','firstname','lastname', 'department','photo')
        labels = {
        "firstname": "First Name","lastname":"Last Name", "department":"Department", "photo": "Photo", "employee_id":"Employee ID"
    }

    def clean_photo(self):

        image = self.cleaned_data['photo']
        im = Image.open(image)

        print("before calling")
        buffered1 = BytesIO()
        im.save(buffered1, format="JPEG")
        face_no, image_drawn = draw_face(buffered1.getvalue())
        print("Face number is: ", face_no)

        #face_no, image_drawn = draw_face(image.file.read())
        #b64_img = base64.b64encode((image_drawn.read())
        buffered2 = BytesIO()
        image_drawn.save(buffered2, format="JPEG")

        b64_img = base64.b64encode(buffered2.getvalue())

        buffered3= BytesIO()
        image_drawn.save(buffered3, format="JPEG")

        
        #Check date is not in past. 
        if face_no ==0:
            raise ValidationError(_('No face detected, please choose another image'))


        return (buffered3, b64_img)


        
       
       
