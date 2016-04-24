# -*- coding: utf-8 -*-
from django import forms
from .models import Rol

"""
Rol form class
"""
class RolForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta : 
        model = Rol
        fields = [ 
            'name', 
            'description',
            'value',
        ]
    #End of meta class
    
#End of Rol form class 