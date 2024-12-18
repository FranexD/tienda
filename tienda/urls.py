from django.urls import path
from . import views  # Esto importa todas las vistas del archivo views.py
from .views import contacto_view  # Esto importa específicamente la vista contacto_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('secundaria/', views.secundaria, name='secundaria'),
    path('contacto/', views.contacto_view, name='contacto'),  # Asegúrate de que esta ruta esté bien
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),  # Vista para el registro de usuarios
   
    path('api/', views.api_consumer, name='api_consumer'),
   path('login/', auth_views.LoginView.as_view(), name='login', kwargs={'next_page': 'home'}),

]

    






