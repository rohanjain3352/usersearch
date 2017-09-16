from django.contrib import admin

# Register your models here.
from .models import User, SearchKeys


class UserAdmin(admin.ModelAdmin):

    search_fields = ['login','created_at']
    list_display = ('login',)

admin.site.register(SearchKeys)
admin.site.register(User, UserAdmin)