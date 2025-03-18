from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreateForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    add_fieldsets = (
        (
            None,
            {
                "fields": ("username", "password1", "password2"),
            },
        ),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )



