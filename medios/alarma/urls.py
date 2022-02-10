from unicodedata import name
from alarma import views
from django.urls import path


urlpatterns =[
    path('', views.vista1,name='vista1'),
    path('aluminio/', views.aluminio, name='aluminio'), 
    path('dt/', views.dt,name='dt'),
    path('Empalme/', views.Empalme, name='Empalme'), 
    path('logout/', views.logout,name='logout'),
    path('PrensaManual/', views.PrensaManual, name='PrensaManual'), 
    path('Principal', views.Principal,name='Principal'),
    path('welding', views.welding, name='welding'), 
    path('wl/', views.wl,name='wl'),
    path('coaxial/',views.coax, name= 'coaxial'),
    path('kawa/',views.kawa, name= 'kawa'),
    path('tw/', views.tw, name='tw'),
    path('prepCoaxial/', views.prepCoaxial, name='prepCoaxial'),
    path('totales/', views.totales, name='totales'),
    
]