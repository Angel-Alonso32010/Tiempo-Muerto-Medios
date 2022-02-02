from alarma import views
from django.urls import path


urlpatterns =[
    path('', views.vista1,name='vista1')
]