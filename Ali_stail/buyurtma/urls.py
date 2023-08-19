from django.urls import path
from .views import *
urlpatterns = [
    path('savat/', SavatView.as_view(), name='savat'),
    path('savat_q/<int:son>/', MiqdorQosh.as_view(), name='qosh'),
    path('savat_k/<int:son>/', MiqdorKamaytir.as_view(), name='kam'),
    path('buyurtma/', BuyurtmaView.as_view(), name='buyurtma'),
    path('qoshish/', BuyurtmaQoshView.as_view(), name='qoshish'),
    path('savatRemove/<int:pk>/', savatRemoveView.as_view(), name='savatRemove'),
    path('Addtanlangan/<int:pk>/', AddtanlanganView.as_view(), name='Addtanlangan'),

]
