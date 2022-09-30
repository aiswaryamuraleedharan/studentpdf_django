from pyexpat import model
from socket import fromshare
from django.forms import ModelForm
from .models import StudentDetails

class StudentDetailsForm(ModelForm):
    class Meta:
        model=StudentDetails
        fields='__all__'

