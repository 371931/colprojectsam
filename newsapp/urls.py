from django.contrib import admin
from django.urls import path, include
from newsapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('ronaldo/', views.page1, name = 'ronaldo'),
    path('gst/', views.page2, name = 'gst'),
    path('chess/', views.page3, name = 'chess'),
    path('zomato/', views.page4, name = 'zomato'),
    path('trade/', views.page5, name = 'trade'),
    path('tai/', views.page6, name = 'tai'),
    path('whatsapp/', views.page7, name = 'whatsapp'),
    path('cwg/', views.page8, name = 'cwg'),
    path('tesla/', views.page9, name = 'tesla'),
]
