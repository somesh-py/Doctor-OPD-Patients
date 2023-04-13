from django.shortcuts import render,redirect
from .models import Issue_Category,DoctorRegistration,PatientRegistration
from django.http import HttpResponse
# Create your views here.

def index(request):
    issue=Issue_Category.objects.all()
    doctor=DoctorRegistration.objects.all()
    return render(request,'patientreg.html',{'issue':issue,'doctor':doctor})

def table(request):
    doctor=DoctorRegistration.objects.all()
    issue=Issue_Category.objects.all()
    patient=PatientRegistration.objects.all()
    return render(request,'table.html',{'doctor':doctor,'issue':issue,'patient':patient})


def patientdata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        issue=request.POST.get('issue')
        issue=Issue_Category.objects.get(id=issue)
        select_doctor=request.POST.get('select_doctor')
        appointment_time=request.POST.get('appointment_time')
        PatientRegistration.objects.create(name=name,contact=contact,email=email,gender=gender,address=address,issue=issue,select_doctor=select_doctor,appointment_time=appointment_time)
    return redirect('/table/')

def patientsall(request,name):
    patients=PatientRegistration.objects.filter(select_doctor=name)
    doctor=DoctorRegistration.objects.get(name=name)
    return render(request,'doctor.html',{'patients':patients,'doctor':doctor})