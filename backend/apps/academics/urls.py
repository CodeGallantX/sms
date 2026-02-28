from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, SubjectViewSet, ExamScoreViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'exam-scores', ExamScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
