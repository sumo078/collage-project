"""
URL configuration for interior project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from interior.settings import BASE_DIR
from interior import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='loginview'),
    # path('saveEnquiry', views.saveEinquery,name='saveEinquery'),
    path('signEnquiry', views.signEinquery,name='signEinquery'),
    #  path('submitform', views.submitform, name='submitform'),
    path('about', views.about, name='about'),
    path('contactinfo', views.contactinfo, name='contactinfo'),
    path('home', views.h , name='home'),
    path('layOut/',views.layOut,  name='layout'),
    path('port/',views.portfolio, name='port'),
    path('booking/',views.bookdata, name='booking'),
    # for furniture
    
    path('furni/',views.furniture, name='furniture'),
    path('categories/',views.all, name='cat'),
    path('inside/',views.the, name='in'),
    path('chair/',views.chair, name='chairs'),
    path('table/',views.table, name='table'),
    path('window/',views.win, name='dow'),
    path('bed/',views.bed, name='bed'),
    path('curtain/',views.curtain, name='curtain'),
    path('sofa/',views.sofa, name='sofa'),
    path('door/',views.do, name='door'),
    path('contact/',views.contact, name='contact'),
    path('thank/',views.thank, name='thank'),
    path('book/',views.book, name='book'),
    path('thanku/',views.thanku, name='thanku'),
    path('magzine/',views.magzine, name='magzine'),
    path('bedroom/',views.bedroom, name='bedroom'),
    path('living/',views.living, name='living'),
    path('kichen/',views.kichen, name='kichen'),
    path('light/',views.light, name='light'),
    path('service/',views.service, name='service'),
    path('pillow/',views.pillow, name='pillow'),
    path('in/',views.interior, name='interior'),
    path('feedback/',views.feedback1, name='feedback'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout1, name='logout')
    
    
     
     
     
     
     
    
   
   
   ]
