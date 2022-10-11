from django.contrib import admin
from .models import donate
from .models import *
# Register your models here.

# Register your models here.
admin.site.register(donate)

class UserForm(admin.ModelAdmin):
    list_display = ['name','email','message']
admin.site.register(UserEnqFrom,UserForm)