from django.urls import path
from .views import *

urlpatterns = [
      path('', HomeView.as_view(), name='home'),
      path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
      path('bolim/<int:soz>/', BolimMahsulotlar.as_view(), name='bolim'),
      path('mahsulot/<int:pk>/', MahsulotDetails.as_view(), name='mahsulot'),
      path('tanlangan/', TanlanganView.as_view(), name='tanlangan'),
      path('remove/<int:pk>/', RemovtanlanganView.as_view(), name='remove'),

]
