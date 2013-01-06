# -*- coding:utf-8 -*-
from django.db import models

#联系人 可以是客户公司的 工厂的 或者其他
class Contact(models.Model):
    "general contact information；m-to-1 with 'Company'"

    GENDER_CHOICES = \
    (
        ('m','male'),
        ('f','female'),
    )
    #名
    first_name = models.CharField(max_length = 64)
    #姓
    last_name = models.CharField(max_length = 64)
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    phone = models.CharField(max_length = 32)
    phone_1 = models.CharField(max_length = 32, blank=True, null=True)
    phone_2 = models.CharField(max_length = 32, blank=True, null=True)
    organization = models.ForeignKey('Organization')

    def __unicode__(self):
        prefix = 'Mr.'
        if(cmp(self.gender, 'm') != 0):
            prefix = 'Ms.'
        return prefix+' '+self.last_name

#组织：客户公司 工厂 合作伙伴 政府等
class Organization(models.Model):
    '''general organization information, can be a client, a factory, 
        goverment department'''

    ORG_TYPE_CHOICES = \
    (
        ('client','client'),
        ('factory','factory'),
        ('government','government'),
        ('ally','ally'),
    )
    #名
    name = models.CharField(max_length = 256)
    #类型
    org_type = models.CharField(max_length = 32, choices=ORG_TYPE_CHOICES)

    def __unicode__(self):
        return self.name

#产品： 定义一个产品
class Product(models.Model):
    "define a general product, to be used in a Inquiry, Contract..."
    
    #材料 选项    
    MATERIAL_CHOICES = \
    (
        ('carbon', 'carbon steel'),    
        ('stainless', 'stainless steel'),
        ('spring', 'spring steel'),    
        ('bearing', 'bearing steel'),
        ('Gcr15', 'Gcr15'),    
        ('A3 steel', 'A3 steel'),
        ('C35', 'C35'),
        ('C45', 'C45'),
    )

    #表面处理 选项
    FINISH_CHOICES = \
    (
        ('phosphating', 'phosphating'),    
        ('plain', 'plain'),
        ('AISI420', 'AISI420'),    
        ('zinc', 'zinc'),
        ('plated', 'plated'),    
        ('oxide black', 'oxide black'),
        ('hot galvanize', 'hot galvanize'),
    )    
    
    #产品型号
    item = models.CharField(max_length = 128)
    #材料类型
    material = models.CharField(max_length = 32, choices = MATERIAL_CHOICES)
    #表面处理
    finish = models.CharField(max_length = 32, choices = FINISH_CHOICES)
    #包装
    packaging = models.CharField(max_length = 1024)
    #产品图纸
    drawing = models.FileField(upload_to='drawing/')



