from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
# Create your views here.


def getdata(request):
    if request.method == "POST":
        data = Student.objects.filter(BoardRollNo=request.POST['bRoll'])
   
        if not data:
            Student.objects.create(
                Name=request.POST['name'],
                BoardRollNo=request.POST['bRoll'],
                RegistrationNo=request.POST['rNo'],
                InstituteRoll=request.POST['iRoll'],
                Technology=request.POST['technology'],
                Shift=request.POST['shift'],
                Group=request.POST['group'],
                Session=request.POST['session'],
                FathersName=request.POST['fname'],
                MothersName=request.POST['mname'],
                Village=request.POST['village'],
                PostOffice=request.POST['pOffice'],
                UpaZila=request.POST['upazila'],
                District=request.POST['district'],
                MobileNo=request.POST['mNo'],
            )
            messages.add_message(
                request, messages.SUCCESS, 'Information add sucsessfully')
        else:
            messages.add_message(
                request, messages.ERROR, 'Data already added with this Roll')

    return render(request, 'icd/getdata.html')
