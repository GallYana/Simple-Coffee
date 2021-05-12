from django.contrib import admin

from .models import *


# admin.site.register(User)
# admin.site.register(Role)
# admin.site.register(News)

admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(News)
admin.site.register(RoleCourses)
admin.site.register(Course)
admin.site.register(CategoryProduct)
admin.site.register(AboutProduct)