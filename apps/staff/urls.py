from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffProfileViewSet, PayrollViewSet, LeaveRequestViewSet

router = DefaultRouter()
router.register(r'profiles', StaffProfileViewSet)
router.register(r'payroll', PayrollViewSet)
router.register(r'leaves', LeaveRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
