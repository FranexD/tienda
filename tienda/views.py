from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ContactoForm
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse





def index(request):
    return render(request, 'index.html')

def secundaria(request):
    productos = Producto.objects.all()
    
    totalItemsCarrito = len(request.session.get('carrito', []))
    return render(request, 'secundaria.html', {'productos': productos, 'totalItemsCarrito':totalItemsCarrito})

@login_required
def contacto(request):
    # Si el formulario ha sido enviado y es válido, guarda los datos
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
    carrito = request.session.get('carrito', []) # Obtiene los datos del navegador.
    producto_en_carrito = next((item for item in carrito if item['id'] == producto.id), None) # Siguiente producto
    
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
    carrito = request.session.get('carrito', [])
    
   
    total = sum(item['precio'] for item in carrito)
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})



def obtener_precio_bitcoin(request):
    # URL de la API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        # Hacer la petición a la API
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la petición falla

        # Parsear la respuesta JSON
        data = response.json()

        # Extraer los datos necesarios
        context = {
            'time_updated': data['time']['updated'],
            'usd_rate': data['bpi']['USD']['rate'],
            'gbp_rate': data['bpi']['GBP']['rate'],
            'eur_rate': data['bpi']['EUR']['rate'],
        }
    except requests.exceptions.RequestException as e:
        # Manejo de errores
        context = {'error': f"No se pudo obtener la información: {str(e)}"}

    # Renderizar el template con los datos
    return render(request, 'precio_bitcoin.html', context)



