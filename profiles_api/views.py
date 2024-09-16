from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers

class TestApi(APIView):
    """afdhasdfhasdfh"""

    serializer_class = serializers.TestSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Kupal si Paz"
        ]

        return Response({'message': 'Kupal kaba?!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message my name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Wassup {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=400
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': "PUT"}) 

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})