"""shop_online_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from shop_online_backend import settings
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import *
from users.views import *
from trade.views import *
from information.views import *
from user_operation.views import *
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'banner',BannerListSet,base_name="bannerIndex")
router.register(r'catelogy',CategoryViewSet,base_name="category")
router.register(r'goods',GoodsViewSet,base_name="good")
router.register(r'integralgoods',integralgoodsViewSet,base_name="integralgoods")
router.register(r'codes',SmsCodeViewset,base_name="codes")
router.register(r'user',UserViewset,base_name='user')
router.register(r'userinfo',UserInfo,base_name="userinfo")
router.register(r'userfavs',UserFavViewset,base_name='userfavs')
router.register(r'address', AddressViewset, base_name="address")
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
router.register(r'IntegralgoodsCart',IntegralgoodsCartViewset,base_name='IntegralgoodsCart')
router.register(r'orders', OrderViewset, base_name="orders")
router.register(r'sendextractnumber',Sendextractnumber,base_name='sendextractnumber')
router.register(r'common',CommonSet,base_name="common")
router.register(r'member',UserMemberViewSet,base_name='member')
router.register(r'alluser',UserProfileViewset,base_name="alluser")
router.register(r'allorder',AllOrderViewSets,base_name='allorder')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include(router.urls)),
    url('^schema/$', schema_view),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title="超市接口")),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
]
