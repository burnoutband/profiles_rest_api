from django.conf.urls import url
from django.conf.urls import include

from profiles_api import views

from rest_framework.routers import DefaultRouter

# Router Setting
router = DefaultRouter()
router.register('hello-viewsettttt', views.HelloViewSet, base_name = 'hello-viewset')


urlpatterns = [
    # /api/hello-view/
    url(r'^hello-view/', views.HelloApiView.as_view()),

    # /api/
    url(r'', include(router.urls))
]