from django.conf.urls import url

from profiles_api import views

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),

]