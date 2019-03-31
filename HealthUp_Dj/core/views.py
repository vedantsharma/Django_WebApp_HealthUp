from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .forms import PresForm
from .models import Prescription

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
            'form': form
    })

def upload(request):
    if request.method == 'POST':
        form = PresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pres_list')
    else:
        form = PresForm()
    return render(request, 'upload.html', {
        'form': form
    })

def pres_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescription_list.html',{
        'prescriptions': prescriptions
    })

def delete_pres(request, pk):
    if request.method == 'POST':
        prescription = Prescription.objects.get(pk=pk)
        prescription.delete()
    return redirect('pres_list')




