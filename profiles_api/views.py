from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        an_apiview = [
            'Uses HTTP method as function',
            'Is similar to traditional Django View'   
            'Gives you most control over your application logic'
        ]
        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else :
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method' : 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})