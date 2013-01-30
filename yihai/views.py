# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

#tracing
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

def my_deck(request):
#    logging.debug(user.get_full_name()+str(user.groups.count()))
    return render_to_response('yihai/my_deck.html', {"request":request})

def home(request):
    #logging.debug(type(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect("/my_deck/")
        #return showWorkDeck(request.user)
    else:
        return HttpResponseRedirect("/log_in/")

@csrf_exempt
def log_in(request):
    ""
    
    if(request.method == 'GET'):        
        return render_to_response('yihai/log_in.html', context_instance=RequestContext(request))       
    elif(request.method == 'POST'):
        user = authenticate(username=request.POST['user_name'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/my_deck/")      
        return render_to_response('yihai/log_in.html', {'hint_error':True})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/log_in/")
    #return HttpResponse("let me go1")


