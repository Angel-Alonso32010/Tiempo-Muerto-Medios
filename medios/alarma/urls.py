from alarma import views
from django.urls import path


urlpatterns =[
    path('', views.vista1,name='vista1'),
    path('', views.aluminio, name='aluminio'), 
    path('', views.dt,name='dt'),
    path('', views.Empalme, name='Empalme'), 
    path('', views.logout,name='logout'),
    path('', views.PrensaManual, name='PrensaManual'), 
    path('', views.Principal,name='Principal'),
    path('', views.welding, name='welding'), 
    path('', views.wl,name='wl'),
    path('',views.coax, name= 'coaxial'),
    path('',views.kawa, name= 'kawa'),
]