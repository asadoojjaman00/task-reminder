from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_active')
    readonly_fields = ('password',)

admin.site.register(User, UserAdmin)

