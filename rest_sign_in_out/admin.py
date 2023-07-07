from django.contrib import admin

from .models import User

class UserClass(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname']

admin.site.register(User, UserClass)
# Register your models here.
