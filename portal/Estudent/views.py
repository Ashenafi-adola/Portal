from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Student_informations, MoreInfo
from .forms import RegistForm
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def mianRegistration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('success')
    else:
        form = UserCreationForm()
    context = {
        "form":form
    }
    return render(request, "Estudent/main_register.html",context)

def success(request):

    return render(request, 'Estudent/success.html',{})

def mainLogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('register')
    context = {

    }
    return render(request, 'Estudent/mainLoginForm.html', context)
@login_required(login_url='mainLogin')
def registration(request):
    form = RegistForm()
    if request.method == "POST":
        form = RegistForm(request.POST,request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('success')

    context = {
        "form":form,
    }
    return render(request,'Estudent/registration.html', context)

def Additional(request):
    students = User.objects.all()
    n = 44334
    if request.method == 'POST':
        for student in students:
            if student.username == "ashu":
                pass
            else:
                student.moreinfo_set.create(
                    user = request.user,
                    Dormitary = "none",
                    AdmissionYear = str(date.today())[:4],
                    Program = "Freshman division",
                    Admission = "Undergraduate",
                    ClassYear = str(date.today())[:4],
                    Section = "4",
                )
                student.username = f'ugr/{n}/18'
                student.save()
                n += 1

    return render(request,'Estudent/complete.html',{})

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("logedin")
            login(request,user)
            return redirect('home')
    return render(request,'Estudent/login.html',{})

@login_required(login_url='login')
def home(request):
    aboutStudent = Student_informations.objects.get(user = request.user)
    moreAboutStudent = MoreInfo.objects.get(user = request.user)
    student = request.user
    context = {
        "a":aboutStudent,
        "m":moreAboutStudent,
        "student":student,

    }
    return render(request,'Estudent/home.html',context)
@login_required(login_url='login')
def studentProfile(request):
    aboutStudent = Student_informations.objects.get(user = request.user)
    moreAboutStudent = MoreInfo.objects.get(user = request.user)
    student = request.user
    context = {
        "a":aboutStudent,
        "m":moreAboutStudent,
        "student":student,

    }
    return render(request, 'Estudent/studprof.html',context)

def appilicant(request):
    aboutStudent = Student_informations.objects.get(user = request.user)
    moreAboutStudent = MoreInfo.objects.get(user = request.user)
    student = request.user
    context = {
        "a":aboutStudent,
        "m":moreAboutStudent,
        "student":student,

    }
    return render(request, 'Estudent/applicant.html',context)