from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from med.forms import MedicineForm
from med.models import Medicine
from .forms import searchForm,guideForm

from django import views
from Chemist_Master.models import ChemistRegister
# Create your views here.

# Using only on function def medi from this view.py

#used For adding new medicines 
def medi(request):
    form=guideForm(request.POST)
    return render(request,'medindex.html',{'form':form})
