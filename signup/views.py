from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from signup.models import Signup,AchivementsManager,Achivement,Stats,Locations
import json
from django.core import serializers
import base64


def api(request):
    if request.method == 'GET':
        return HttpResponse('allo')
    elif request.method == 'POST':
        data = request.body
        result = json.loads(data)
        error = 'Bad Json.'
        try:
            print result
            if result['query'] == 'createSignup':
                name = result['name']
                surname = result['surname']
                image = result['image']
                password = result['password']
                email = result['email']
                gender = result['gender']
                s = Signup(email = email, name = name, surname = surname, password = password, gender = gender)
                s.save()

                a = AchivementsManager(signup = s, name = email)
                a.save()
                a1 = Achivement(manager =a, name ='5potato', description = 'jouer 5 fois')
                a1.save()
                a2 = Achivement(manager =a, name ='25potato', description = 'jouer 25 fois')
                a2.save()
                a3 = Achivement(manager =a, name ='50potato', description = 'jouer 50 fois')
                a3.save()
                #hack cree les achivements c'est pas inteligent live la. 
                st = Stats(signup = s,numbersOfWin=0,numbersOfFail=0,timesPlayed=0,achivementsUnlocked=0)
                st.save()
                error = 'Could not save to the databse.'

                path = '/root/projet1/static/img/profile/'
                futureImg = open(path+email+'.png','wb')
                imgData = base64.b64decode(image)
                futureImg.write(imgData)

                return HttpResponse(request.body)

            elif result['query'] == 'deleteSignup':
                email = result['email']
                profile = Signup.objects.filter(email = email).delete()
                return HttpResponse('deleted ' + email)

            elif result['query'] == 'selectSignup':
                email = result['email']
                profile = Signup.objects.filter(email = email).values()[0]
                return HttpResponse(json.dumps(profile))

            elif result['query'] == 'signupExist':
                email = result['email']
                s = list(Signup.objects.filter(email = email))  
                print s  
                return HttpResponse(str(s != []))

            elif result['query'] == 'updateAchivement':
                email = result['email']
                profile = Signup.objects.filter(email = email)[0]
                am = AchivementsManager.objects.filter(signup = profile)[0]
                name = result['name']
                state = result['state']
                a = Achivement.objects.filter(manager = am, name = name, unlocked = state)[0]
                a.save()
                return HttpResponse(name + " " + state)

            elif result['query'] == 'updateProfile':
                name = result['name']
                surname = result['surname']
                password = result['password']
                email = result['email']
                gender = result['gender']

                s = Signup.objects.filter(email = email)[0]
                s.name = name
                s.surname = surname
                s.password = password
                s.gender = gender

                s.save()
                return HttpResponse('updated ' + email)

            elif result['query'] == 'updateStats':
                email = result['email']
                s = Signup.objects.filter(email = email)[0]
                st = Stats.objects.filter(signup = s)[0]
                st.numbersOfWin = result['numbersOfWin']
                st.numbersOfFail = result['numbersOfFail']
                st.timesPlayed = result['timesPlayed']
                st.achivementsUnlocked = result['achivementsUnlocked']
                st.save()
                return HttpResponse('updated ' + email)

            elif result['query'] == 'getStats':
                email = result['email']
                s = Signup.objects.filter(email = email)[0]
                stats = Stats.objects.filter(signup = s).values()[0]
                return HttpResponse(json.dumps(stats))

            elif result['query'] == 'updateLocations':
                email = result['email']
                lat = result['lat']
                lng = result['lng']
                s = Signup.objects.filter(email = email)[0]
                l = Locations(signup = s,lat=lat,lng=lng)
                l.save()
                return HttpResponse('added locations: ' + str(lat) + ' ' + str(lng))

            elif result['query'] == 'getLocations':

                email = result['email']
                s = Signup.objects.filter(email = email)[0]
                locations = Locations.objects.filter(signup = s)

                googleData = []
                for idx,loc in enumerate(locations):
                    googleData.append(['',loc.lat,loc.lng,idx])

                return HttpResponse(googleData)

            elif result['query'] == 'getAchivements':

                email = result['email']
                s = Signup.objects.filter(email = email)[0]
                am = AchivementsManager.objects.filter(signup = s)[0]

                achivements = Achivement.objects.filter(manager=am)
                data = serializers.serialize('json',achivements)

                return HttpResponse(data)

        except Exception,e:
                print str(e)
                return HttpResponse(error)







