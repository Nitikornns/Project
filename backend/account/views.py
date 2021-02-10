from rest_framework.viewsets import ModelViewSet
from .models import Account
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated


class AccountsViewSet(ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
