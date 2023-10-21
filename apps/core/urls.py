from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.core.views import DashboardViewSetOne, DashboardViewSetSecond
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("dashboards-one", DashboardViewSetOne, basename="dashboard_one")
router.register("dashboards-second", DashboardViewSetSecond, basename="dashboard_sec")

urlpatterns = [
                  path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
