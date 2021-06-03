from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

# def index(request):
#     return HttpResponse("Marks Distribution Application!!!!")

def user(request):
    marks_list = Student.objects.order_by('Marks_obtained') 
    marks_dict= {'marks_info': marks_list}
    return render(request, 'Student_Page.html', context=marks_dict)