from django.urls import path, include
from profiles_api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet) 
#we don't need to provide basename as it automatically setup with the name of
# model name provided in queryset in UserProfileViewSet i.e., a type of ModelViewSet.

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]