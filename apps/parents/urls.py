from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentProfileViewSet, ParentStudentRelationshipViewSet

router = DefaultRouter()
router.register(r'profiles', ParentProfileViewSet)
router.register(r'relationships', ParentStudentRelationshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
