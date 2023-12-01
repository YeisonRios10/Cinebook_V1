//se define la funcion a utilizar para la carga de peliculas
const cargarPeliculas = async () => {
  try {
    const respuesta = await fetch(
      "https://api.themoviedb.org/3/movie/popular?api_key=a36a0107dd6b1ea8569d698315062324"
    ); //API con ApiKey

    //console.log(respuesta); con esto se muestra la respuesta de la consulta

    if (respuesta.status === 200) {
      //200 es que está OK la consulta
      const datos = await respuesta.json(); //la respuesta se guarda en la variable datos y se transforma a formato json
      console.log(datos); //para mostrar el resultado de la respuesta del json
      const topFive = 5; // variable para mostrar una parte del array

      let peliculasHTML = "";

      for (let i = 0; i < topFive && i < datos.results.length; i++) {
        // un ciclo for para recorrer el array de results con las pelis
        const pelicula = datos.results[i];
        peliculasHTML += `
                    <div class="destacada">
                        <img class="desta" src="https://image.tmdb.org/t/p/w500/${pelicula.poster_path}">
                        <span>${pelicula.title}<span>
                    </div>`;

        // console.log("Top de cinco pelis", pelicula.title);
      }
      document.getElementById("destacada").innerHTML = peliculasHTML;
    } else if (respuesta.status === 401) {
      console.log("no existe la peli");
    }
  } catch (error) {
    console.log("Error", error);
  }
};
cargarPeliculas();

/* ==============S E S I O N ========================================  */
function validarFormulario2(e) {
  e.preventDefault();

  const correo = document.getElementById("correo").value;
  const contrasenia = document.getElementById("contrasenia").value;
  const confirmContrasenia = document.getElementById("confirm-contrasenia").value;
  const nombreUsuario = document.getElementById("nombre-usuario").value;
  const fechaNacimiento = document.getElementById("fecha-nacimiento").value;
  const genero = document.getElementById("genero").value;
  const terminos = document.getElementById("check-terminos").checked;

  const validarCorreo = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/;
  const validarContrasenia = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*]).{8,}/;

  let errorText = "";

  if (correo === "") {
    errorText += "El campo Correo es obligatorio\n";
  } else if (!validarCorreo.test(correo)) {
    errorText += "El campo Correo no tiene un formato válido\n";
  }

  if (contrasenia === "") {
    errorText += "El campo Contraseña es obligatorio\n";
  } else if (!validarContrasenia.test(contrasenia)) {
    errorText +=
      "La contraseña debe tener al menos 8 caracteres, con al menos un dígito, una mayúscula, una minúscula y un carácter especial.\n";
  }

  if (confirmContrasenia === "") {
    errorText += "El campo Confirmar Contraseña es obligatorio\n";
  } else if (confirmContrasenia !== contrasenia) {
    errorText += "Las contraseñas no coinciden\n";
  }

  if (nombreUsuario === "") {
    errorText += "El campo Nombre de Usuario es obligatorio\n";
  }

  if (fechaNacimiento === "") {
    errorText += "El campo Fecha de nacimiento es obligatorio\n";
  } else {
    const fechaNac = new Date(fechaNacimiento);
    const hoy = new Date();
    const edad = hoy.getFullYear() - fechaNac.getFullYear();

    if (edad < 18) {
      errorText += "Debes ser mayor de 18 años para registrarte.\n";
    }
  }

  if (genero === "") {
    errorText += "El campo Género es obligatorio\n";
  }

  if (!terminos) {
    errorText += "Debes aceptar los términos y condiciones\n";
  }

  if (errorText !== "") {
    alert(errorText);
    return false;
  } else {
    alert("Su registro fue exitoso.");
    document.getElementById("correo").value = "";
    document.getElementById("contrasenia").value = "";
    document.getElementById("confirm-contrasenia").value = "";
    document.getElementById("nombre-usuario").value = "";
    document.getElementById("fecha-nacimiento").value = "";
    document.getElementById("genero").value = "";
    document.getElementById("check-terminos").checked = false;  // Corrección aquí
    return true;  // Cambiado de false a true si el formulario está destinado a ser enviado.
  }
}
