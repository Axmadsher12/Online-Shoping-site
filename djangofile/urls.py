"""djangofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from myfiles.views import *
from djangofile import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name='about'),
    path('codes/',codes,name='codes'),
    path('faq/',faq,name='faq'),
    path('icons/',icons,name='icons'),
    path('',index,name='index'),
    path('mail/',mail,name='mail'),
    path('mobiles/',pro,name='products'),
    path('gadgets/',pro1,name='products1'),
    path('appliances/',pro2,name='products2'),
    path('single/',single1,name='single'),

    path('mobiles_color/<rang>/', color_mobils, name='color_mobiles'),
    path('mobiles_price/<price>/', price_mobils, name='price_mobiles'),

    path('compyuter_color/<rang1>/',color_Computer,name='color_compyuter'),
    path('compyuter_price/<price1>/',price_compyuter,name='price_compyuter'),

    path('single1/<id>/',single_mobile,name='single1'),
    path('single3/<id>/',single_compyuter,name='single3'),
    path('single2/<id>/',single_appliance,name='single2'),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL,document_root = settings.MEDIAFILES_DIRS)
