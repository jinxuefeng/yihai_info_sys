# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
#from sales.models import Inquiry, Category, Quiz

def index(request):
    pass
'''
    course_list = Course.objects.all()
    category_list = Category.objects.all()
    quiz_list = Quiz.objects.all()
    return render_to_response('gikoo/index.html', {'course_list': course_list, 'category_list': category_list,
'quiz_list': quiz_list})
'''

def detail(request, object_id):
    pass
'''
    course = get_object_or_404(Course, pk=object_id)
    return render_to_response('gikoo/course_detail.html', {'object': course})
'''
