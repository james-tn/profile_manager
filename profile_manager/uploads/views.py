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


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)


        if form.is_valid():
            image = form.cleaned_data['photo']
            image_drawn = draw_face(image.file.read())
            form.save()
            #b64_img = base64.b64encode((image_drawn))
            #mime = "image/jpg"
            #mime = mime + ";" if mime else ";"
            #input_image = "data:%sbase64,%s" % (mime, b64_img)        

            return render(request, 'view_form.html', {
        'form': form, 'image_drawn':image_drawn
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

