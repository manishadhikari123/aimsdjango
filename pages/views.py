from django.shortcuts import render
from .models import Training

# Create your views here.



def gallery(request):
    
    trains = Training.objects.all() 

    return render(request,'gallery.html', {'trains': trains})

