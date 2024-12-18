document.addEventListener("DOMContentLoaded", () => {
  const botonesAgregar = document.querySelectorAll(".btn-agregar");
  const cartCount = document.getElementById("cart-count");

  let carrito = 0;

  botonesAgregar.forEach((boton) => {
    boton.addEventListener("click", () => {
      carrito++;
      cartCount.textContent = carrito;

      // Animación de éxito al agregar
      boton.style.backgroundColor = "#68b0ab";
      boton.textContent = "¡Agregado!";
      setTimeout(() => {
        boton.style.backgroundColor = "#ffcb77";
        boton.textContent = "Agregar al carrito";
      }, 1000);
    });
  });
});

// cart.js
document.addEventListener('DOMContentLoaded', () => {
  const cartCountElement = document.getElementById('cart-count');
  const cart = JSON.parse(localStorage.getItem('cart') || '[]');
  cartCountElement.innerText = cart.length;

  const addToCartButtons = document.querySelectorAll('.btn-agregar');
  addToCartButtons.forEach(button => {
    button.addEventListener('click', () => {
      const productoId = button.getAttribute('id');
      const productoNombre = button.getAttribute('nombre');
      const productoPrecio = button.getAttribute('precio');

      const producto = { id: productoId, nombre: productoNombre, precio: productoPrecio };
      cart.push(producto);
      localStorage.setItem('cart', JSON.stringify(cart));

      cartCountElement.innerText = cart.length;
    });
  });
});
