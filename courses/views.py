from django.shortcuts import render
from .models import *

def show_course(request, course_id):
    modules = Module.objects.filter(parent=course_id)

    return render(request, 'courses/courses.html', {'modules': modules})

def show_module(request, module_id):
    lections = Lection.objects.filter(parent=module_id)
    return render(request, 'courses/modules.html', {"lections": lections})

def show_lection(request, lection_id):
    lcontent = LectionContent.objects.filter(parent=lection_id)
    return render(request, 'courses/lection.html', {"lec": lcontent})
