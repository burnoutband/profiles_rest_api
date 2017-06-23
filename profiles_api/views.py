from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers

# Create your views here.


class HelloApiView(APIView):
    """Test API View."""

    # 이 APIView 의 시리얼라이저는 요놈이다라고 Django or DRF 에게 알려줌
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        # DRF는 Response를 JSON Format 으로 이쁘게 보여줌 (변경은 아님).
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message.
        Or List of the Objects in the database.
        """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message.
        Or Insert a object in the database.
        """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID (database)."""

        return Response({'http_method': "GETt"})


    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUTt'})


    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCHh'})


    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETEe'})