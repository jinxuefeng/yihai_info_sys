from django.http import HttpResponse
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from models import *
from serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
'''
class JSONResponse(HttpResponse):
    
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
'''
'''
@api_view(['GET','POST'])
def organization_list(request, format = None):
    " "

    if request.method == 'GET':
        orgs = Organization.objects.all()
        serializer = OrganizationSerializer(orgs)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #data = JSONParser.parse(request)
        serializer = OrganizationSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class OrgList(generics.ListCreateAPIView):
    model = Organization
    serializer_class = OrganizationSerializer

class ContactList(generics.ListCreateAPIView):
    model = Contact
    serializer_class = ContactSerializer

    

