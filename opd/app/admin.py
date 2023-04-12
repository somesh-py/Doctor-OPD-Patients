from django.contrib import admin
from .models import Issue_Category,DoctorRegistration,PatientRegistration
# Register your models here.


@admin.register((Issue_Category))
class Issue_CategoryModelAdmin(admin.ModelAdmin):
    list_display=['id','Category_name']

@admin.register((DoctorRegistration))
class DoctorRegistrationModelAdmin(admin.ModelAdmin):
    list_display=['id','name','specialist','gender','experiance','available','appointment','image','address']


@admin.register((PatientRegistration))
class PatientRegistrationModelAdmin(admin.ModelAdmin):
    list_display=['id','name','contact','email','gender','address','issue','select_doctor','appointment_time']
