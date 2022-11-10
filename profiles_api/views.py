from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format = None):
        an_apiview = [
            'Uses HTTP method as function',
            'Is similar to traditional Django View'   
            'Gives you most control over your application logic'
        ]
        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})