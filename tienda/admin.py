from django.contrib import admin
from .models import Producto, Contacto  # Asegúrate de importar los modelos correctos

# Registrar el modelo Producto
admin.site.register(Producto)
# Registrar el modelo Contacto si deseas que se pueda administrar desde el admin también
admin.site.register(Contacto)
