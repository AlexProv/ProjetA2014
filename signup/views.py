from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from signup.models import Signup as signup
import json

def api(request):
    if request.method == 'GET':
        return HttpResponse('allo')
    elif request.method == 'POST':
        data = request.body
        result = json.loads(data)
        error = 'Bad Json.'
        try:
            if result['query'] == 'signup':

                name = result['name']
                surname = result['surname']
                image = result['image']
                password = result['password']
                email = result['email']

                s = signup(email = email, name = name, surname = surname, image = image, password = password)
                s.save()
                error = 'Could not save to the databse.'
                return HttpResponse(request.body)
            elif result['query'] == 'delete':

                email = result['email']
                profile = signup.objects.filter(email = email).delete()

                return HttpResponse('deleted' + email)
            elif result['query'] == 'select':

                email = result['email']
                profile = signup.objects.filter(email = email).values()[0]

                return HttpResponse(json.dumps(profile))
        except Exception,e:
                print str(e)
                return HttpResponse(error)