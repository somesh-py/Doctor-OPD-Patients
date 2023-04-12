from django.db import models

# Create your models here.

GENDER_CHOICES=(
    ('male','male'),
    ('female','female')
)

APPOINTMENT_TIME = (
    ('10:00 AM TO 11:00 AM', '10:00 AM TO 11:00 AM'),
    ('11:10 AM TO 12:00 PM', '11:10 AM TO 12:00 PM'),
    ('1:00 PM TO 2:00 PM', '1:00 PM TO 2:00 PM'),
    ('2:10 PM TO 3:00 PM', '2:10 PM TO 3:00 PM'),
    ('3:10 PM TO 4:00 PM', '3:10 PM TO 4:00 PM'),
    ('4:10 PM TO 5:00 PM', '4:10 PM TO 5:00 PM'),
    ('6:00 PM TO 7:00 PM', '6:00 PM TO 7:00 PM')
)

class Issue_Category(models.Model):
    Category_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.Category_name
    

class DoctorRegistration(models.Model):
    name=models.CharField(max_length=50)
    specialist=models.ForeignKey(Issue_Category,on_delete=models.CASCADE)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=50)
    experiance=models.CharField(max_length=50)
    available=models.BooleanField()
    appointment=models.CharField(choices=APPOINTMENT_TIME,max_length=100)
    image=models.ImageField(upload_to="doctor_image")
    address=models.CharField(max_length=100)

class PatientRegistration(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=50)
    address=models.CharField(max_length=50)
    issue=models.ForeignKey(Issue_Category,on_delete=models.CASCADE)
    select_doctor=models.CharField(max_length=100)
    appointment_time=models.CharField(choices=APPOINTMENT_TIME,max_length=100)
