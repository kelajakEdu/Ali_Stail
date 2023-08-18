from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeLoginsizView.as_view(), name='loginsiz'),
    path('home/', include('asosiy.urls')),
    path('user/', include('userapp.urls')),
    path('buyurtma/', include('buyurtma.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
