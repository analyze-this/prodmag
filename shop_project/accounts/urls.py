from django.urls import path
from .views import *


app_name = 'accounts'
urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]