from django.contrib import admin
from models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('client', 'time')
    ordring = ['time']
    search_feilds = ('client', 'time')
#    list_filter = ('status',)

admin.site.register(Inquiry, InquiryAdmin)



