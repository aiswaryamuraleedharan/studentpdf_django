from django.urls import path
from .import views
from .views import GeneratePdf

urlpatterns = [
    path('',views.StudentPage,name='student'),
    path('studentdetails/',views.StudentDetailsPage,name='studentdetails'),
    path('pdf/', GeneratePdf.as_view(),name='pdf'),
]