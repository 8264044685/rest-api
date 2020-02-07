from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import status
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