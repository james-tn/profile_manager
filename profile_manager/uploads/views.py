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
from django.shortcuts import get_object_or_404


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })





def create_profile(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        employee_id=""

        if form.is_valid():
            image_validator, origin_image, image_drawn = form.cleaned_data['photo']
            #def the uploaded image has 1 face and is valid
            if (image_validator==1):
                record = Document()
                record.photo=origin_image
                record.firstname=form.cleaned_data['firstname']
                record.lastname=form.cleaned_data['lastname']
                record.department=form.cleaned_data['department']

                record.save()
                employee_id=record.employee_id

            buffered = BytesIO()


        #face_no, image_drawn = draw_face(image.file.read())

            image_drawn.save(buffered, format="JPEG")
            b64_img = base64.b64encode((buffered.getvalue()))
            one_face= image_validator==1
            #multi_face = image_validator>1
            no_face = image_validator==0

    


            return render(request, 'view_form.html', {
        'form': form, 'image_drawn':b64_img,'one_face':one_face, 'no_face': no_face, 'employee_id': employee_id
    })

    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
def search_profile(request, pk):

    if pk != '':
        
        doc = get_object_or_404(DocumentForm, pk=pk)

        form = DocumentForm(request.POST, isinstance=Document)

        if form.is_valid():
            image_validator, origin_image, image_drawn = form.cleaned_data['photo']
            buffered = BytesIO()



            image_drawn.save(buffered, format="JPEG")
            b64_img = base64.b64encode((buffered.getvalue()))




        return render(request, 'search_result_form.html', {
        'form': form,'image_drawn':b64_img
    })

    else:
        form = DocumentForm()
    return render(request, 'search_form.html', {
        'form': form
    })


