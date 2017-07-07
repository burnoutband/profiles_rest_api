# References
# print("request.method = {}".format(request.method))
# print("request.user.id = {}".format(request.user.id))
# print("request.user.is_superuser = {}".format(request.user.is_superuser))
# print("request.user.is_staff = {}".format(request.user.is_staff))
# print("request.user.is_authenticated()= {}".format(request.user.is_authenticated()))

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, )

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles. ModelViewset Creates, Reads, update object on model."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)  # 끝에 , 는 python이 tuple인지 인식하는 장치이다.


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handels creating, reading and updating profile feed items."""


    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    # permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated,)

    def get_queryset(self):
        """Return Resource after checking permission which I have."""

        if self.request.user.is_superuser:
            queryset = models.ProfileFeedItem.objects.all()
            print("Case : admin")
        else:
            print("Case : Non admin")
            queryset = models.ProfileFeedItem.objects.filter(id=self.request.user.id)

        return queryset



    # Object를 create 할 때, 수행하는 로직을 커스터마이즈 할 경우 perform_create 함수 사용
    # 여기서는 로그인 유저에 한해서 생성되는 user feed item 이 user profile 에 제대로 셋팅되는지 확실히 하기 위해 사용함.
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
