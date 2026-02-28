from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App modules
    path('api/v1/accounts/', include('apps.accounts.urls')),
    path('api/v1/students/', include('apps.students.urls')),
    path('api/v1/parents/', include('apps.parents.urls')),
    path('api/v1/staff/', include('apps.staff.urls')),
    path('api/v1/academics/', include('apps.academics.urls')),
    path('api/v1/finance/', include('apps.finance.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/ai/', include('apps.ai.urls')),
]
