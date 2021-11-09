from django.urls import path
from . import views

urlpatterns = [
    # Login views
    path('login/', views.user_login, name='login')
]