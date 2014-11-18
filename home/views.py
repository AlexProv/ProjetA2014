from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response

def home(request):
	#if request.method == 'GET':
    dicto = {'name':'allo','email':'fuck'}
    return render_to_response("home/home.html",dicto)
