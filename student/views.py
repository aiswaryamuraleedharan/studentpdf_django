from multiprocessing import context
from django.shortcuts import render,redirect
from student.forms import StudentDetailsForm
from .models import StudentDetails
from django.views.generic import View
from .process import html_to_pdf
from django.http import HttpResponse
# Create your views here.
def StudentPage(request):
    form = StudentDetailsForm()
    context = {'form':form}
    if request.method == 'POST':
        form1 = StudentDetailsForm(request.POST)
        if form1.is_valid():
            form1.save()    
            return redirect('student')
    return render(request,'student.html',context)

def StudentDetailsPage(request):
    data = StudentDetails.objects.all()
    context = {'data':data}
    return render(request,'studentdetails.html',context)

class GeneratePdf(View):
    def get(self,request,*args,**kwargs):

         # getting the template
        data=StudentDetails.objects.all()
        context={'data':data}
        pdf = html_to_pdf('studentdetails.html',context)

         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')