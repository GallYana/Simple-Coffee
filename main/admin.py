from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import *


# admin.site.register(User)
# admin.site.register(Role)
# admin.site.register(News)

class EmployeeInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

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

admin.site.register(Lection)
admin.site.register(Module)
admin.site.register(Course)

admin.site.register(CategoryProduct)
admin.site.register(AboutProduct)