from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from trade.models import OrderInfo
from trade.serializers import AllOrderSerializer,AllOrderDetailSerializer
from users.serializers import UserProfileSerializer
from user_operation.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# Create your views here.
class AllOrderViewSets(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = OrderInfo.objects.all()
    serializer_class = AllOrderSerializer
    # authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AllOrderDetailSerializer

        return AllOrderSerializer


class UserProfileViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    这个是获取所有的用户信息，所以不用增加任何权限
    list:
        获取所有的用户
    """
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication )