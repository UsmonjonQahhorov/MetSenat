from rest_framework.routers import DefaultRouter
from sponsors.views import SponsorViewSet

router = DefaultRouter()
router.register("sponsors", SponsorViewSet, basename="sponsors")

urlpatterns = router.urls
