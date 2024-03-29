"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from main.views import (HeaderView,SlayderView,ChoiseView,ProductView,AdvantagesView,
                        ReservationView,CostView,RequirementsView,InsuranceView,AdditionalView)
from django.conf.urls.i18n  import i18n_patterns

router = routers.DefaultRouter()
router.register('header_list',HeaderView)
router.register('slayder_list',SlayderView)
router.register('choise_list',ChoiseView)
router.register('product_list',ProductView)
router.register('reservation_list',ReservationView)
router.register('cost_list',CostView)
router.register('requirements_list',RequirementsView)
router.register('insurance_list',InsuranceView)
router.register('additional_list',AdditionalView)
router.register('advantages_list',AdvantagesView)

urlpatterns = [
    path('adm/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/auth/',include('rest_framework.urls')),
    path('',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(path('', include('main.urls')))