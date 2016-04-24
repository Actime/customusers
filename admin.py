"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Wednesday, January 6, 2016
"""

# Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Rol, UserSystem 
from .forms import RolForm

"""
Rol admin
For display the model on the admin module of the system
"""
class RolAdmin( admin.ModelAdmin ) :
    
    form = RolForm
    list_display = [ 
        "__unicode__", 
        "name", 
        "description", 
        "timestamp", 
        "updated",
    ]
    
# End Rol admin class

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserSystemInline( admin.StackedInline ) :
    
    model = UserSystem
    can_delete = False
    verbose_name_plural = 'usersystem'

# End of UserSystem Inline class

"""
User Admin
"""
class UserAdmin( BaseUserAdmin ) :
    
    inlines = ( UserSystemInline, )
    
# End of User Admin class

# Export all the admin classes to the admin site view
admin.site.register( Rol, RolAdmin )
admin.site.unregister(User)
admin.site.register(User, UserAdmin)