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
            origin_image, drawn_image = form.cleaned_data['photo']
            record = Document()
            record.department = form.cleaned_data['department']
            record.firstname = form.cleaned_data['firstname']
            record.lastname = form.cleaned_data['lastname']
            record.photo = origin_image.read()

            record.save()



            return render(request, 'view_form.html', {
        'form': form, 'image_drawn':drawn_image
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

