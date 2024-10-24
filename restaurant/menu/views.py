from django.shortcuts import render
from menu.models import Food
# Create your views here.
def home(request):
    result=Food.objects.all()
    return render(request,'index.html',{'res': result}) 


