/* === esta  primera línea del documneto garantiza que todos los elemntos del html esten cargados en el DOM   */
document.addEventListener("DOMContentLoaded", function () {

  /* ==============P O P U P ========================================  */
  const title = document.getElementById("title");
  const popup = document.getElementById("popup");

  title.addEventListener("mouseover", () => {
    popup.style.display = "block";
  });

  title.addEventListener("mouseout", () => {
    popup.style.display = "none";
  });

/* ==============B O T O N   S C R O L L ========================================  */
// Obtén el botón de scroll
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Agrega un evento al botón para detectar cuando se hace clic
scrollToTopBtn.addEventListener("click", () => {
  // Desplázate al inicio de la página suavemente
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});

// Muestra u oculta el botón según la posición del scroll
window.addEventListener("scroll", () => {
  if (window.pageYOffset > 100) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
});




});
/* esto cierra la funcion del DOM*/
