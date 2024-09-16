from django.urls import path

from profiles_api import views

urlpatterns = [
    path('test-view/', views.TestApi.as_view()),
]