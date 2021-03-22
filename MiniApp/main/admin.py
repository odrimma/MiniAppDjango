from django.contrib import admin
from django import forms
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'patronymic', 'info', 'created_at', 'updated_at')


admin.site.register(User, UserAdmin)





