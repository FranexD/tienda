from django.urls import path
from . import views  # Esto importa todas las vistas del archivo views.py
from .views import contacto # Esto importa específicamente la vista contacto_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('secundaria/', views.secundaria, name='secundaria'),
    path('contacto/', views.contacto, name='contacto'),  # Asegúrate de que esta ruta esté bien
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('api/', views.api_consumer, name='api_consumer'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]







