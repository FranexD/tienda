from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ContactoForm
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests




def index(request):
    return render(request, 'index.html')

def secundaria(request):
    productos = Producto.objects.all()
    return render(request, 'secundaria.html', {'productos': productos})

@login_required
def contacto(request):
    # Si el formulario ha sido enviado y es válido, guarda los datos
    print("CONTACTOSSSS")
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')  # Redirige al mismo formulario después de enviar

    # Si es un GET o después de guardar, pasa los contactos existentes
    form = ContactoForm()
    contactos = Contacto.objects.all()  # Obtiene todos los contactos registrados
    return render(request, 'contacto.html', {'form': form, 'contactos': contactos})

def agregar_al_carrito(request, producto_id):
    print("Productos en carrito")
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', [])
    producto_en_carrito = next((item for item in carrito if item['id'] == producto.id), None)
    
    print(producto_en_carrito)
    if producto_en_carrito:
        messages.info(request, f'El producto {producto.nombre} ya está en el carrito.')
    else:
        carrito.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'imagen': producto.imagen.url,
        })
        messages.success(request, f'El producto {producto.nombre} ha sido agregado al carrito.')

    request.session['carrito'] = carrito
    return redirect('secundaria')

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    carrito = [item for item in carrito if item['id'] != producto_id]
    request.session['carrito'] = carrito
    messages.success(request, 'Producto eliminado del carrito.')
    return redirect('carrito')

def vaciar_carrito(request):
    request.session['carrito'] = []
    messages.success(request, 'El carrito ha sido vaciado.')
    return redirect('carrito')




# def contacto(request):
#     if request.method == 'POST':
#         form = ContactoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
#             return redirect('contacto')
#     else:
#         form = ContactoForm()
#     return render(request, 'contacto.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirigir al índice después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})



def carrito(request):
    carrito = request.session.get('cart', [])
    #for value in carrito:
    print(carrito)
   
    total = sum(item['precio'] for item in carrito)
    
    
    return render(request, 'carrito.html', {'cart': carrito, 'total': total})


def api_consumer(request):
    # URL de la API externa que deseas consumir
    api_url = 'https://api.externa.com/data'
    response = requests.get(api_url)

    # Verificar que la respuesta sea exitosa
    if response.status_code == 200:
        data = response.json()  # Convertir la respuesta a formato JSON
    else:
        data = None

    return render(request, 'api_consumer.html', {'data': data})
