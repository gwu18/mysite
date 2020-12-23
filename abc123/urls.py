#used for processing url thats being passed in
from django.urls import path

from . import views

app_name = 'abc123'
urlpatterns = [
    path('', views.index, name='index'),
    # path('webpage2', views.webpage2, name='webpage2'), # www.garywu.com/webpage2
    ]