# -*- coding:utf-8 -*-
from django.db import models

#一个可以联系的组织或者个人
class Contactable(models.Model):
    "a contactable person or org, all ways to contact it"
    
    #地址
    addr = models.CharField(max_length = 1024, blank=True, null=True)
    #邮编
    zip = models.CharField(max_length = 32, blank=True, null=True)
    phone = models.CharField(max_length = 32, blank=True, null=True)
    phone1 = models.CharField(max_length = 32, blank=True, null=True)
    phone2 = models.CharField(max_length = 32, blank=True, null=True)
    QQ = models.CharField(max_length = 32, blank=True, null=True)
    email = models.CharField(max_length = 32, blank=True, null=True)
    msn = models.CharField(max_length = 32, blank=True, null=True)
    skype = models.CharField(max_length = 32, blank=True, null=True)
    others = models.CharField(max_length = 128, blank=True, null=True)

    class Meta:
        abstract=True


#普遍意义上的联系人 可以是销售的客户，采购的工厂等等
class Contact(Contactable):
    "general contact information；m-to-1 with 'Company'"

    GENDER_CHOICES = \
    (
        ('m','male'),
        ('f','female'),
    )
    #名 可以为空
    first_name = models.CharField(max_length = 64, blank=True, null=True)
    #姓
    last_name = models.CharField(max_length = 64)
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True)
    #title: sales?manager?boss?
    title = models.CharField(max_length = 32, blank=True, null=True)

    class Meta:
        abstract=True

    def __unicode__(self):
        prefix = 'Mr.'
        if(cmp(self.gender, 'm') != 0):
            prefix = 'Ms.'
        return prefix+' '+self.last_name

#普遍意义的组织：可以是销售的客户公司，采购的工厂等等
class Organization(Contactable):
    '''general organization information, can be a client, a factory, 
        goverment department'''

    #名
    name = models.CharField(max_length = 256)
    #所在国籍
    nation = models.CharField(max_length = 128, blank=True, null=True)

    class Meta:
        abstract=True

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

class ClientCompany(Organization):
    "a client company"
    
    #客户公司情况描述
    desc = models.CharField(max_length = 128, blank=True, null=True)

class ClientStaff(Contact):
    "a client company's staff information"
        
    #客户公司联系人情况描述
    desc = models.CharField(max_length = 128, blank=True, null=True)
    company = models.ForeignKey(ClientCompany)
    
    

#ProductUnit(询价中的一个<产品,数量>集合)
class Set(models.Model):
    "m-to-1 with Inquiry"

    #产品
    product_type = models.OneToOneField(Product)
    #数量
    quantity = models.PositiveIntegerField(default=0)
    #所属订单
    inquiry = models.ForeignKey('Inquiry')

#Inpuiry(客户询价记录)
class Inquiry(models.Model):
    "record all clients' inquiries"

    #询价时间
    time = models.DateTimeField()
    #客户公司
    client = models.ForeignKey(ClientCompany, verbose_name="client's name", )
    #询价人
    contact = models.ForeignKey(ClientStaff)
    #备注
    remark =  models.CharField(max_length = 2048)


    def __unicode__(self):
        return 'quiry from '+unicode(self.client)+' '+str(self.time)

