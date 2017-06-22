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

from api_core.views import ProyectDonationViewSet, UserDonationViewSet, FundingDonationViewSet

router = SimpleRouter()
router.register(r'api/donacion/proyecto', ProyectDonationViewSet)
router.register(r'api/donacion/usuario', UserDonationViewSet)
router.register(r'api/donacion/fondeo', FundingDonationViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
