# -*- coding:utf-8 -*-
from django.db import models

#ProductUnit(询价中的一个<产品,数量>集合)
class Set(models.Model):
    "m-to-1 with Inquiry"

    #产品
    product_type = models.OneToOneField('info.Product')
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
    client = models.ForeignKey('info.Organization',verbose_name="client's name", )
    #询价人
    contact = models.ForeignKey('info.Contact')
    #备注
    remark =  models.CharField(max_length = 2048)


    def __unicode__(self):
        return 'quiry from '+unicode(self.client)+' '+str(self.time)

