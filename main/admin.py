from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import *


class EmployeeInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module', 'module_name', 'parent', 'order_course')
    list_display_links = ('module', 'module_name')

class LectionsAdmin(admin.ModelAdmin):
    list_display = ('lection', 'topic', 'parent')
    list_display_links = ('lection', 'topic')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'created_date', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'topic')
    list_editable = ('is_published',)
    fields = ('topic', 'news_text', 'photo', 'get_html_photo', 'role','created_date', 'published_date', 'is_published')
    readonly_fields = ('created_date', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Миниатюра"


admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель Simple Coffee'

admin.site.unregister(User)

admin.site.register(User, UserAdmin)

admin.site.register(Role)
admin.site.register(News, NewsAdmin)

admin.site.register(Lection, LectionsAdmin)
admin.site.register(LectionContent)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Course)

admin.site.register(CategoryProduct)
admin.site.register(AboutProduct)