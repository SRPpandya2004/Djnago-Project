# Register your models here.

from django.contrib import admin
from .models import User

# admin.site.site_header = "Movie booking System"
# admin.site.site_title = "Movie system"
# admin.site.index_title = "Site of Movie System"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'username', 'contact_number')

