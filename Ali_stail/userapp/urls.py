from django.urls import path
from .views import *
# from asosiy.views import *

urlpatterns = [
      # path('', HomeView.as_view()),
      path('login/', LoginView.as_view(), name='login'),
      path('logout/', LogoutView.as_view(), name='logout'),
      path('register/', RegisterView.as_view(), name='register'),
      path('ProfAdd/', ProfAddView.as_view(), name='ProfAdd'),
]
