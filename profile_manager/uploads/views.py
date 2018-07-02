from django.shortcuts import render

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


def update_profile(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        employee_id = ''
        if form.is_valid():
            image_validator, origin_image, image_drawn = form.cleaned_data['photo']
            #def the uploaded image has 1 face and is valid
            if (image_validator==1):
                print(request.POST)
                employee_id = form.cleaned_data['employee_id']
                record = Document.objects.get(employee_id=employee_id)
                record.photo=origin_image
                record.firstname=form.cleaned_data['firstname']
                record.lastname=form.cleaned_data['lastname']
                record.department=form.cleaned_data['department']

                record.save()

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
    return render(request, 'create_form.html', {
        'form': form
    })


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
    return render(request, 'create_form.html', {
        'form': form
    })
def search_profile(request):
    

    employee_id = request.GET['employee_id']
    if (employee_id!=""):
        print("employee id is", employee_id)
        try:
            doc = Document.objects.get(employee_id=employee_id)
        except:
            return render(request, 'search_form.html', {'error_employee_id':employee_id})


        firstname = doc.firstname
        lastname = doc.lastname
        department = doc.department
        id = doc.employee_id
        image = doc.photo
        _, image_drawn = draw_face(image.file.read())

        buffered = BytesIO()



        image_drawn.save(buffered, format="JPEG")
        b64_img = base64.b64encode((buffered.getvalue()))




        return render(request, 'search_result_form.html', {
    'image_drawn':b64_img, 'employee_id': doc.employee_id, 'firstname': firstname, 'lastname': lastname, 'department': department
})

    else:
        return render(request, 'search_form.html')


