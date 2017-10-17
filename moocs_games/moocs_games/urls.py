"""moocs_games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from games.views import ROFR, JUDO,Company_Merger,Price_War, jump
from rest_framework.routers import DefaultRouter
from games import views

router = DefaultRouter()
router.register(r'ROFR', views.ROFR_ViewSet)
router.register(r'JUDO', views.JUDO_ViewSet)
router.register(r'Company_Merger', views.Company_Merger_ViewSet)
router.register(r'Price_War', views.Price_War_ViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ROFR/', ROFR),
    url(r'^JUDO/', JUDO),
    url(r'^Price_War/', Price_War),
    url(r'^Company_Merger/', Company_Merger),
    url(r'^jump/', jump),
    url(r'^api/', include(router.urls))
]
