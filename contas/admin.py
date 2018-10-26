from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('custom_email', 'username')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('custom_email', 'username', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('custom_email', 'password')}),
        ('Informações Pessoais', {'fields': ('username',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)