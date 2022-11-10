from django.urls import path
from profiles_api.views import *

urlpatterns = [
    path('hello-view/', HelloApiView.as_view())
]