from django import template
from courses.models import *

register = template.Library()

    
@register.simple_tag()
def get_modules(filter=None):
    if not filter:
        return Module.objects.all()
    else:
        return Module.objects.filter(module_name=filter)

@register.simple_tag()
def get_lections(filter=None):
    if not filter:
        return Lection.objects.all()
    else:
        return Lection.objects.filter(topic=filter)

@register.simple_tag()
def get_lec(filter=None):
    if not filter:
        return Lection.objects.all()
    else:
        return Lection.objects.filter(parent=filter)
        
@register.simple_tag()
def get_lo(filter=None):
    if not filter:
        return LectionContent.objects.all()
    else:
        return LectionContent.objects.filter(parent=filter)