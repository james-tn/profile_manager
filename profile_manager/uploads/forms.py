from django import forms

from uploads.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'employee_id','firstname','lastname', 'department','photo')
        labels = {
        "firstname": "First Name","lastname":"Last Name", "department":"Department", "photo": "Photo", "employee_id":"Employee ID"
    }
        firstname = forms.CharField(label='Fist Name', max_length=100)
        lastname = forms.CharField(label='Last Name', max_length=100)
        department = forms.CharField(label='Department', max_length=100)
        photo = forms.ImageField(label ='Photo')
        employee_id = forms.CharField(label ='Employee ID',  max_length=100,required=False)
        
       
       
