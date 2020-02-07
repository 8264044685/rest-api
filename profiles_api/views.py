from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
# Create your views here.

class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializers.HelloSerializer
	def get(self, request, format=None):
		"""Return a list of APIView features"""
		an_apiview = [
			'Users THHP methods as function (get, post, petch, put, delete)',
			'Is similar to the django traditional view',
			'Gives you the most control over you application logic',
			'is mapped manually to urls'			
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})

	def post(self, request):
		"""Data post"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'hello {name}'

			return Response({'message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BED_REQUEST)

	def put(self, request, pk=None):
		""""Data put"""
		return Response({'method': 'PUT'})

	def patch(self, request, pk=None):
		"""Data patch mathod"""
		return Response({'method': 'PATCH'})

	def delete(self, request, pk=None):
		"""Data delete method"""
		return Response({'method': 'DELETE'})



class HelloViewSets(viewsets.ViewSet):
	"""Test API View Set"""

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Retun a hello message"""
		a_viewsets = [
			'A HelloViewSets for Create, retirieve, Update, partial_Update, Destroy'
			'Automatically map to Urls using Routers',
			'Provide more functionally with less code'
		]

		return Response({'message':'Hello!', 'a_viewsets':a_viewsets})

	def create(self, request):
		"""Create a new hello message"""
		serializer = self.serializer_class(data = request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}!'
			return Response({'message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BED_REQUEST)

	def retrieve(self, request, pk=None):
		""""Hendle getting an objects by ts IDS"""
		return Response({'http_method':'GET'})

	def update(self, request, pk=None):
		"""Handel updating an objects """
		return Response({'http_method':'PUT'})

	def partial_update(self, request, pk=None):
		"""Handle update part of an objects"""
		return Response({'http_method':'PATCH'})

	def destroy(self, request, pk=None):
		"""Handle delete ojects"""
		return  Response({'http_method':'DELETE'})


class UserPofileViewSets(viewsets.ModelViewSet):
	"""Handle creating and updating userprofiles"""
	serializer_class = serializers.UserProfileSerializer

	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('username', 'email',)