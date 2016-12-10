# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers

# Rest framework imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Import classes 
from .models import Rol, UserSystem
# Import Serializers
from .serializers import RolSerializer, UserSystemSerializer, UserSerializer

"""
Rol List Api View
Object list and creation
"""
class RolList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Rol.objects.all()
    # Serializer class
    serializer_class = RolSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function
# End of Rol List class

"""
Rol Detail Api View
"""
class RolDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Rol.objects.all()
    # Serializer class
    serializer_class = RolSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Rol Detail class
    
"""
User System List Api View
Object list and creation
"""
class UserSystemList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = UserSystem.objects.all()
    # Serializer class
    serializer_class = UserSystemSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of User System List class

"""
User System Detail Api View; returns with the id of the user not the usersystem
"""
class UserSystemDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Security stuff
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = UserSystem.objects.all()
    # Serializer class
    serializer_class = UserSystemSerializer
    # get the object with the pk
    def get_object( self, pk ) :
        """ This returns an object with the pk """
        try :
            # Get the object by userid
            return UserSystem.objects.get( user = pk )
        except UserSystem.DoesNotExist :
            # return 404 error if not found in the db
            raise Http404
    # End of get_object function
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object( kwargs['pk'] )
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of User System Detail class

"""
UserList Api View
Object list and creation
"""
class UserList( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = User.objects.all()
    # Serializer class
    serializer_class = UserSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of Category List by Competition class

"""
User detail
view for getting the detail, update and destroy user
"""
class UserDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = User.objects.all()
    # Serializer class
    serializer_class = UserSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of UserDetail class

"""
Register competitor number
this will return the next competitor number of the event
"""
class UserSystemByUserId( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = UserSystem.objects.all()
    # Serializer class
    serializer_class = UserSystemSerializer
    # Get custom object
    def get_object( self, pk ) :
        """
        Get object funciton
        This will return a competition
        """
        try :
            # Get the object by the primary key
            return UserSystem.objects.get( user = pk )
        except UserSystem.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object( self.request.GET['user_id'] )
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of RegisterCompetitorNumber api view class

"""
User login
This will return the user if it is validated
"""
class UserLogin( generics.CreateAPIView ) :
    # Authentication classes
    authentication_classes = ( BasicAuthentication, )
    # Query set variable
    queryset = User.objects.all()
    # Serializer variable
    serializer_class = UserSerializer
    
    def get_object( self, user_name ) :
        """
        Function that retrieves the object with the sending user_name
        """
        try :
            # Get the object by the primary key
            return User.objects.get( username = user_name )
        except User.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def create(self, request, *args, **kwargs):
        """
        Create function
        This will just work for our custom post function
        hehe pretty lazy if you ask me :)
        """
        # Serialize the object we have
        user = User()
        user.username = request.data["username"]
        user.password = request.data["password"]
        print( user.username, " " , user.password )
        # Need to get the user from the username we have 
        user_from_db = self.get_object( user.username )
        # Data variable
        data = {
            "data" : None
        }
        # Validate the user_from_the_db
        if user_from_db is not None :
            # Validate password
            if user_from_db.check_password( user.password ) :
                # Return the hole user
                data["data"] = { 
                    "pk" : user_from_db.id,
                    "username" : user_from_db.username,
                    "email" : user_from_db.email,
                    "password" : user.password
                }
                response = Response(data)
                return response 
            else :
                data["data"] = { "error" : "Password didn't match." }
                # Return the response data empty
                return Response( data, status=status.HTTP_404_NOT_FOUND )
        else :
            # Return the response data empty
            data[ "data" ] = { "error" : "This user doesn't exist." }
            return Response( data, status=status.HTTP_404_NOT_FOUND )
        # End of user validation
    # End of create function
# End of UserLogin class
