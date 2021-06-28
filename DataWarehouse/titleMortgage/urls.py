from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

# router.register('api/title-mortgage', TitleMortgageViewSet, 'titleMortgage')

urlpatterns = router.urls
