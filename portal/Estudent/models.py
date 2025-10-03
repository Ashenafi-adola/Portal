from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student_informations(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    MARITAL_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    REGION_CHOICES = [
        ('Addis Ababa', 'Addis Ababa'),
        ('Afar Region', 'Afar Region'),
        ('Amhara Region', 'Amhara Region'),
        ('Benishangul-Gumuz Region', 'Benishangul-Gumuz Region'),
        ('Central Ethiopia Region', 'Central Ethiopia Region'),
        ('Dire Dawa', 'Dire Dawa'),
        ('Gambela Region', 'Gambela Region'),
        ('Harari Region', 'Harari Region'),
        ('Oromia Region', 'Oromia Region'),
        ('Sidama Region', 'Sidama Region'),
        ('Somali Region', 'Somali Region'),
        ('South Ethiopia Region', 'South Ethiopia Region'),
        ('South West Ethiopia Peoples\' Region', 'South West Ethiopia Peoples\' Region'),
        ('Tigray Region', 'Tigray Region'),
    ]
    TUITION_CHOICES = [
        ('cost_sharing', 'cost_sharing'),
        ('non-cafe', 'non-cafe'),
    ]
    DISABILITY_CHOICES = [
        ('None', 'No Disability'),
        ('Physical', 'Physical Disability'),
        ('Hearing', 'Hearing Impairment'),
        ('Visual', 'Visual Impairment'),
        ('Other', 'Other (Please specify)'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Father = models.CharField(max_length=30)
    Grand_Father = models.CharField(max_length=30)
    ሙሉ_ስም = models.CharField(max_length=30)
    Gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    Marital_Status = models.CharField(max_length=20,choices=MARITAL_CHOICES)
    Matric_Result = models.IntegerField()
    Date_Of_Birth = models.DateField()
    Age = models.IntegerField()
    Place_Of_Birth = models.CharField(max_length=30)
    Photo = models.ImageField(null=True, upload_to='photos/')
    Nationality = models.CharField(max_length=20)
    Region = models.CharField(max_length=50, choices=REGION_CHOICES)
    Disability = models.CharField(max_length=30, choices=DISABILITY_CHOICES)
    Email = models.EmailField(unique=True)
    Phone = models.IntegerField()
    Registration_Number = models.IntegerField(null=True)
    Tuition_Type = models.CharField(max_length=20, choices=TUITION_CHOICES)
    Country = models.CharField(max_length=20)
    Street_Address = models.CharField(max_length=20, null=True)                  
    Home_Tel_Phone = models.IntegerField(null=True)
    Mobile = models.IntegerField(null=True)
    Work_Tel_Phone = models.IntegerField(null=True)
    Woreda = models.CharField(null=True)
    Kebele = models.CharField(null=True)
class MoreInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Dormitary = models.CharField(max_length=10,)
    AdmissionYear = models.CharField(max_length=10,null=True)
    Program = models.CharField(max_length=255,null=True)
    Admission = models.CharField(max_length=255,null=True)
    ClassYear = models.CharField(20,null=True)
    Section = models.CharField(20,null=True)
