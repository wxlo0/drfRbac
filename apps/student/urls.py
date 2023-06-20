from django.urls import include, path
from rest_framework import routers
from .views import ClassViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
