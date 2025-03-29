from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SavePDFView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itinerary/', views.itinerary, name='itinerary'),  # Add a trailing slash
    path('travel-plan/', views.travel_plan, name='travel_plan'),
    path('save_pdf_view/', SavePDFView.as_view(), name='save_pdf_view'),
    path('ex', views.explo, name='explo1'),
    path('hotelcbe', views.hcbe, name='hotelcbe'),
    path('hotel1cbe', views.h1cbe, name='hotel1cbe'),
    path('hotel2cbe', views.h2cbe, name='hotel2cbe'),
    path('hotel3cbe', views.h3cbe, name='hotel3cbe'),
    path('restcbe', views.rcbe, name='restcbe'),
    path('hidcbe', views.hicbe, name='hidcbe'),
    path('ex2', views.explo2, name='explo2'),
    path('chhtl', views.chtl, name='chhtl'),
    path('chhtl1', views.chtl1, name='chhtl1'),
    path('chhtl2', views.chtl2, name='chhtl2'),
    path('chhtl3', views.chtl3, name='chhtl3'),
    path('cfms', views.cfamous, name='cfms'),
    path('chat', views.ch1, name='chat'),
    path('cres', views.crs, name='cres1'),
    path('chid', views.chd, name='chid'),
    path('cfam', views.cfa, name='cfam'),
    path('cha1', views.ch1, name='cha1'),
    path('chid', views.chd, name='chid'),
    path('result1', views.result1, name='result1'),
    path('result2', views.result2, name='result2'),
] 

