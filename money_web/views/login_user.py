# To change this template, choose Tools | Templates
# and open the template in the editor.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def login_user(request):
    username = password = ''
    if request.POST:
        
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        print username

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                print "LOGUEADO EXITOSO"
            else:
                state = "Your account is not active, please contact the site admin."
                print "CUENTA INACTIVA"
        else:
            state = "Your username and/or password were incorrect."
            print "CREDENCIALES INCORRECTAS"            
    
    return render_to_response('index.html',{},context_instance=RequestContext(request))
