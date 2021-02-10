from django.urls import path

from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('accounts', AccountsViewSet),

urlpatterns = router.urls
