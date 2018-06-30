from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import base64
from uploads.models import Document
from uploads.forms import DocumentForm
from uploads.faceDetector import draw_face
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })





def create_profile(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)


        if form.is_valid():
            origin_image, image_drawn = form.cleaned_data['photo']
    #def clean_photo(self):
            record = Document()
            record.photo=origin_image
            record.firstname=form.cleaned_data['firstname']
            record.lastname=form.cleaned_data['lastname']
            record.department=form.cleaned_data['department']

            record.save()

            buffered = BytesIO()


        #face_no, image_drawn = draw_face(image.file.read())

            image_drawn.save(buffered, format="JPEG")
            b64_img = base64.b64encode((buffered.getvalue()))

        
        #Check date is not in past. 



            return render(request, 'view_form.html', {
        'form': form, 'image_drawn':b64_img
    })
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
def model_form_edit(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm(request.POST, request.FILES)
    return render(request, 'view_form.html', {
        'form': form
    })

