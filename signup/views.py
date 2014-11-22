from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from signup.models import Signup
from signup.models import AchivementsManager
from signup.models import Achivement
from signup.models import stats as Stats
import json

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
                s = Signup(email = email, name = name, surname = surname, image = image, password = password, gender = gender)
                s.save()

                a = AchivementsManager(signup = s, name = email)
                a.save()
                a1 = Achivement(manager =a, name ='5Star', description = 'jouer 5 fois')
                a1.save()
                a2 = Achivement(manager =a, name ='2Row', description = 'jouer 2 fois dans la meme journee')
                a2.save()
                a3 = Achivement(manager =a, name ='Joueur', description = 'Joindre le monde de selfilock')
                a3.save()
                #hack cree les achivements c'est pas inteligent live la. 

                error = 'Could not save to the databse.'
                return HttpResponse(request.body)

            elif result['query'] == 'deleteSignup':

                email = result['email']
                profile = Signup.objects.filter(email = email).delete()

                return HttpResponse('deleted' + email)
            elif result['query'] == 'selectSignup':

                email = result['email']
                profile = Signup.objects.filter(email = email).values()[0]

                return HttpResponse(json.dumps(profile))

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
                image = result['image']
                password = result['password']
                email = result['email']
                gender = result['gender']

                s = Signup.objects.filter(email = email)[0]
                s.name = name
                s.surname = surname
                s.image = image
                s.password = password
                s.gender = gender

                s.save()
                return HttpResponse(json.dumps(s))

            elif result['query'] == 'updateStats':
                email = result['email']
                s = Signup.objects.filter(email = email)[0]
                st = Stats.objects.filter(Signup = s)[0]
                st.numbersOfWin = result['numbersOfWin']
                st.numbersOfFail = result['numbersOfFail']
                st.timesPlayed = result['timesPlayed']
                st.achivementsUnlocked = result['achivementsUnlocked']
                st.save()
            elif result['query'] == 'getStats':
                email = result['email']
                s = Signup.objects.filter(email = email)[0]
                st = Stats.objects.filter(Signup = s)[0]

                stats = Stats.objects.filter(email = email).values()[0]
                return HttpResponse(json.dumps(stats))
            elif result['query'] == 'getAchivements':
                email = result['email']
                s = Signup.objects.filter(email = email)
                am = AchivementsManager.objects.filter(signup = s)

                achivements = Achivement.objects.filter(manager=am).values()
                answer = []
                for o in achivements:
                    answer.append(json.dumps(o))

                return HttpResponse(json.dumps(answer))

        except Exception,e:
                print str(e)
                return HttpResponse(error)







