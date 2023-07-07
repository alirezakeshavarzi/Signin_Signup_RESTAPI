from django.contrib import admin

from .models import User

class UserClass(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname', 'username', 'email', 'phone','password']

admin.site.register(User, UserClass)
# Register your models here.
