from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewsets', views.HelloViewSets, base_name='hello-viewsets')
router.register('profile', views.UserPofileViewSets)


urlpatterns = [
	path('',views.HelloApiView.as_view()), 
	path('view-sets/',include(router.urls)),

]	