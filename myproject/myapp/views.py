from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name' : 'Puzan',
          'age' : 20,
          'nationality' : 'Nepali',
    }
    return render(request,'index.html',context)