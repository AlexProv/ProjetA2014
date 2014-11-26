from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from signup.models import Signup
from signup.models import Stats
from django.http import HttpResponse

def home(request):
	#if request.method == 'GET':
    dicto = {'name':'allo','email':'bollo'}

    pl = Signup.objects.all()

    profiles = []
    for o in pl:
        name = o.surname + ' ' + o.name 
        email = o.email 

        s = Stats.objects.filter(signup = o)[0]

        profiles.append([name,email,s.numbersOfWin,s.numbersOfFail,s.timesPlayed])

    dicto['profiles'] =profiles
    return render_to_response("home/base.html",dicto)

def profile(request):
    return render_to_response("home/landing.html",{})

def simon(request):
    return render_to_response("home/profile.html",{})
