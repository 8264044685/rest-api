from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
	"""name field for testing a APIView"""
	name = serializers.CharField(max_length = 20)

class UserProfileSerializer(serializers.ModelSerializer):
	"""UserProfile model serializers"""

	class Meta:
		model = models.UserProfile
		fields = ['id', 'email', 'username', 'password']



		extra_kwargs = {
			'password' : {
				'write_only': True,
				'style' : {'input_type': 'password'}
			}
		}

	def create(self, validated_data):
		"""Create and return a new user"""
		user = models.UserProfile.objects.create_user(
				email = validated_data['email'], 
				username = validated_data['username'],
				password = validated_data['password'],

			)

		
		return user