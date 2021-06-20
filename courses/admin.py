from django.contrib import admin
from .models import *

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module', 'module_name', 'parent', 'order_course')
    list_display_links = ('module', 'module_name')

class LectionsAdmin(admin.ModelAdmin):
    list_display = ('lection', 'topic', 'parent', 'order_lection')
    list_display_links = ('lection', 'topic')

class LectionContentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'content')
    list_display_links = ('parent',)

admin.site.register(Lection, LectionsAdmin)
admin.site.register(LectionContent, LectionContentAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Course)