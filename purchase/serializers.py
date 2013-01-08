from models import *
from rest_framework import serializers
" "

class OrganizationSerializer(serializers.ModelSerializer):
    " "    
    
    class Meta:
        model = Organization
        fields = ('name',)


class ContactSerializer(serializers.ModelSerializer):
    " "    
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'gender', 'phone', 'organization')


