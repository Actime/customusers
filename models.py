# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""

# Imports
from django.db import models
from django.contrib.auth.models import User

"""
Rol model
Model for the user admin roles
"""
class Rol( models.Model ) :
    
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    value = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.name
    # End of unicode function
    
# End of Rol model class

"""
User System
Model that inher from the user model, this is for the admin application as you register yourself
"""
class UserSystem( models.Model ) :
    
    user = models.OneToOneField( User, on_delete=models.CASCADE )
    rol = models.ForeignKey( Rol, default = 1 )
    user_name = models.CharField( max_length = 200, default = '' )
    birth_date = models.DateField( blank = True, default = '' )
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return ("{0}").format(self.user)
    # End of unicode function
# End of User System class