# -*- coding:utf-8 -*-
from django.db import models
from sales.models import Organization, Contact

class Factory(Organization):
    "a factory"
    
    #工厂情况描述
    desc = models.CharField(max_length = 128, blank=True, null=True)

class FactoryStaff(Contact):
    "a factory staff information"
        
    #工厂联系人情况描述
    desc = models.CharField(max_length = 128, blank=True, null=True)




