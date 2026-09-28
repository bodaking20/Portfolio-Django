from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scripts/', views.scripts_list, name='scripts_list'),
    path('scripts/<int:id>/', views.script_detail, name='script_detail'),
    path('websites/', views.websites_list, name='websites_list'),
    path('websites/<int:id>/', views.website_detail, name='website_detail'),
]

