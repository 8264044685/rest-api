from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
	"""Allow user to edit their own profle"""

	def has_object_permission(self, request, view, obj):
		"""Check user is trying toedittheirown profile"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.id == request.user.id

class UserUpdateOwnStatus(permissions.BasePermission):
	"""Allow user to update their own status"""
	def has_object_permission(self, request, view, obj):
		"""Check the use to trying toupdate their status"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user_profile.id == request.user.id