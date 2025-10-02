from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import Student_informations, MoreInfo
from .forms import RegistForm
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

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
        user = authenticate(request,username=username, password= password)
        if user is not None:
            login(user)
            return redirect('register')
    return render(request,'Estudent/mainLoginForm.html',{})


key = 0
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username, password= password)
        if user is not None:
            login(user)
            return redirect('home')

    return render(request, "Estudent/login.html", {})

def registration(request):
    if request.method == 'POST':
        form = RegistForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return render(request, "Estudent/main_register.html",context)
    else:
        form = RegistForm()
        
    return render(request, "Estudent/registration.html",{"form":form})

def Additional(request):
    students = User.objects.all()
    n = 76387
    pk = 1
    for student in students:
        if student not in MoreInfo.objects.all():
            student.moreinfo_set.create(
                Password = str(n),
                Identity_Card = f"ugr/{n}/18",
                Dormitary = "B371 R32",
                AdmissionYear = str(date.today()),
                Program =  "Freshman Program",
                Admission = "Undergraduate",
                ClassYear =  str(date.today()),
                Section =  3,
                No = pk,
            )
            student.username = f'ugr/{n}/18'
            student.password = str(n)
            student.No = pk
            student.save()
            pk += 1
            n += 1
    return HttpResponse("registration compelete")
def home(request):
    a = Student_informations.objects.get(No=key)
    return render(request, "Estudent/home.html",{"a":a,"b":b})
def studentProfile(request):
    a = Student_informations.objects.get(No=key)
    return render(request, "Estudent/studprof.html", {"a":a,"b":b})
def appilicant(request):
    a = Student_informations.objects.get(No=key)
    return render(request, "Estudent/applicant.html", {"a":a, "b":b})