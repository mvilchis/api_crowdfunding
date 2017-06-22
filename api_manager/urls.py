"""api_manager URL Configuration

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
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url
from django.contrib import admin

from api_core.views import ProjectDonationViewSet, UserDonationViewSet, FundingDonationViewSet
from api_core.views import ProjectRecompesasViewSet, UserRecompensasViewSet, FundingRecompensasViewSet
from api_core.views import ProjectCapitalViewSet, UserCapitalViewSet, FundingCapitalViewSet
from api_core.views import ProjectDeudaViewSet, UserDeudaViewSet, FundingDeudaViewSet

router = SimpleRouter()
router.register(r'api/donacion/proyecto', ProjectDonationViewSet)
router.register(r'api/donacion/usuario', UserDonationViewSet)
router.register(r'api/donacion/fondeo', FundingDonationViewSet)

router.register(r'api/recompensas/proyecto', ProjectRecompesasViewSet)
router.register(r'api/recompensas/usuario', UserRecompensasViewSet)
router.register(r'api/recompensas/fondeo', FundingRecompensasViewSet)

router.register(r'api/capital/proyecto', ProjectCapitalViewSet)
router.register(r'api/capital/usuario', UserCapitalViewSet)
router.register(r'api/capital/fondeo', FundingCapitalViewSet)

router.register(r'api/deuda/proyecto', ProjectDeudaViewSet)
router.register(r'api/deuda/usuario', UserDeudaViewSet)
router.register(r'api/deuda/fondeo', FundingDeudaViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
