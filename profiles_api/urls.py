from django.conf.urls import url
from django.conf.urls import include

from profiles_api import views

from rest_framework.routers import DefaultRouter

# "Router Setting"
# when we register model viewset, we don't need to specify the base name.
# Because DRF automatically figure this out by looking at the model that's registered with the serializer that
# is registered on our viewset.

router = DefaultRouter()
router.register('hello-viewsettttt', views.HelloViewSet, base_name = 'hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    # /api/hello-view/
    url(r'^hello-view/', views.HelloApiView.as_view()),

    # /api/
    url(r'', include(router.urls))
]

