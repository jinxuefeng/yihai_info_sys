# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

#tracing
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

def showWorkDeck(user):
    logging.debug(user.get_full_name()+str(user.groups.count()))
    return HttpResponse("welcome"+user.last_name)

def home(request):
    #logging.debug(type(request))
    if request.user.is_authenticated():
        return showWorkDeck(request.user)
    else:
        return HttpResponseRedirect("/log_in/")

@csrf_exempt
def log_in(request):
    ""
    
    if(request.method == 'GET'):
        return render_to_response('yihai/log_in.html')        
    elif(request.method == 'POST'):
        return render_to_response('yihai/log_done.html', context_instance=RequestContext(request))


