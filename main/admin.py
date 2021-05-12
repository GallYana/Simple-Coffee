from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

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

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(News)
admin.site.register(RoleCourses)
admin.site.register(Course)
admin.site.register(CategoryProduct)
admin.site.register(AboutProduct)