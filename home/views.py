from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from signup.models import Signup
from signup.models import Stats,Locations
from django.http import HttpResponse

def home(request):
	#if request.method == 'GET':
    dicto = {'name':'allo','email':'bollo'}

    pl = Signup.objects.all()

    profiles = []
    for o in pl:
        name = o.surname + ' ' + o.name 
        email = o.email 
        gender = o.gender

        s = Stats.objects.filter(signup = o)[0]
        imgpath = 'assets/img/profile/'+email+'.png'
        profiles.append([name,email,gender,s.numbersOfWin,s.numbersOfFail,s.timesPlayed,s.achivementsUnlocked,imgpath])

    dicto['profiles'] =profiles
    return render_to_response("home/base.html",dicto)

def landing(request):
    return render_to_response("home/landing.html",{})

def simon(request):
    return render_to_response("home/profile.html",{})

def profile(request,email):
    try:
        s = Signup.objects.filter(email = email)[0]
        dictio = {}
        dictio['name'] = s.surname + ' ' + s.name
        dictio['email'] = email
        dictio['gender'] = s.gender
        dictio['imgpath'] = 'assets/img/profile/'+email+'.png'

        st = Stats.objects.filter(signup = s)[0]

        dictio['nbPlayed'] = st.timesPlayed
        dictio['nbWin'] = st.numbersOfWin
        dictio['nbLose'] = st.numbersOfFail
        dictio['nbAchiev'] = st.achivementsUnlocked
        
        locations = Locations.objects.filter(signup=s)
        googleData = []
        for idx,loc in enumerate(locations):
            googleData.append([0,float(loc.lat),float(loc.lng),idx])

        dictio['coords'] = googleData
        print googleData

        return render_to_response("home/profile.html",dictio)
    except: 
        return HttpResponse('Email dose not exist! asshole')


def tester(request):
    dictio = {}
    dictio['imgpath'] = 'assets/img/profile/'+'qwwe@h.com'+'.png'
    dictio['email'] = 'qwwe@h.com'
    dictio['end'] = '.png'
    return render_to_response("home/lol.html",dictio)


