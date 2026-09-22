from django.contrib import admin

from .models import User

class UserClass(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'phone']

admin.site.register(User, UserClass)
# Register your models here.
