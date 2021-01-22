from django.urls import path

from rest_framework import routers

from account.views import *

router = routers.SimpleRouter()
router.register('account', AccountsViewSet),

urlpatterns = router.urls
