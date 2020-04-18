from rest_framework import routers
from .api import LeadViewSet

routers = routers.DefaultRouter()

routers.register('api/lead',LeadViewSet,"lead")

urlpatterns = routers.urls