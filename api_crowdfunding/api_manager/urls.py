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
from rest_framework.authtoken import views

from api_core.views import (ProjectDonationViewSet,
                            ProjectRecompesasViewSet,
                            ProjectCapitalViewSet,
                            ProjectDeudaViewSet,
                            UserDonationViewSet,
                            UserCapitalViewSet,
                            UserRecompensasViewSet,
                            UserDeudaViewSet, 
                            FundingRecompensasViewSet,
                            FundingDonationViewSet,
                            FundingCapitalViewSet,
                            FundingDeudaViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/donacion/proyecto', ProjectDonationViewSet.as_view()),
    url(r'^api/donacion/usuario', UserDonationViewSet.as_view()),
    url(r'^api/donacion/fondeo', FundingDonationViewSet.as_view()),
    url(r'^api/recompensas/proyecto', ProjectRecompesasViewSet.as_view()),
    url(r'^api/recompensas/usuario', UserRecompensasViewSet.as_view()),
    url(r'^api/recompensas/fondeo', FundingRecompensasViewSet.as_view()),
    url(r'^api/capital/proyecto', ProjectCapitalViewSet.as_view()),
    url(r'^api/capital/usuario', UserCapitalViewSet.as_view()),
    url(r'^api/capital/fondeo', FundingCapitalViewSet.as_view()),
    url(r'^api/deuda/proyecto', ProjectDeudaViewSet.as_view()),
    url(r'^api/deuda/usuario', UserDeudaViewSet.as_view()),
    url(r'^api/deuda/fondeo', FundingDeudaViewSet.as_view()),

]
