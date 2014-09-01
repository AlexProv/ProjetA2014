from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Line

# Create your views here.
from django.http import HttpResponse

def home(request):
    for l in Line.objects.all():
        print l.text
    return render_to_response("story/home.html", {'lines': Line.objects.all()})


library = {} 

def register(f):
    library[f.__name__] = f 
    return f 

@register 
def myfunc():
    pass

