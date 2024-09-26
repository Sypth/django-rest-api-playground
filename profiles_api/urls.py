from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('test-viewset', views.TestViewSet, basename='test-viewset'),
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    path('test-view/', views.TestApi.as_view()),
    path('', include(router.urls)),

]
