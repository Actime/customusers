# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""

# Imports
from rest_framework import serializers
from .models import Rol, UserSystem
from django.contrib.auth.models import User

"""
Rol Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Users
"""
class RolSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = Rol
        fields = (
            'id',
            'name',
            'description', 
            'value', 
        )
    # End of Meta class
    
# End of Rol Serializer class

"""
UserSystem Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Users
"""
class UserSystemSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = UserSystem
        fields = (
            'id',
            'user',
            'rol', 
            'birth_date',    
        )
    # End of Meta class
    
# End of User System Serializer class

class UserSerializer( serializers.ModelSerializer ) :
    
    class Meta :
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
            "is_staff",
            "last_login",
            "password",
            "email",
            "date_joined",
            "pk",
        )
    # End of Met class
    
# End of User serializer class