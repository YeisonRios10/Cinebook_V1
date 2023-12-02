const URL = "http://127.0.0.1:5000/";

document.getElementById('formulario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitamos que se envíe el formulario

    const nombre = document.getElementById("nombre");
    const correo = document.getElementById("correo");
    const contrasenia = document.getElementById("contrasenia");
    const parrafo = document.getElementById("warnings");

    let warnings = "";
    let entrar = false;
    let regexEmail = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/;
    
    parrafo.innerHTML = "";

    if (nombre.value.length < 6) {
        warnings += 'El nombre no es válido <br>';
        entrar = true;
    }

    if (!regexEmail.test(correo.value)) {
        warnings += 'El correo no es válido <br>';
        entrar = true;
    }

    if (contrasenia.value.length < 8) {
        warnings += 'La contraseña no es válida <br>';
        entrar = true;
    }

    if (entrar) {
        parrafo.innerHTML = warnings;
    } else {
        // Si las validaciones son exitosas, procedemos con el envío del formulario

        var formData = new FormData();
        formData.append('nombre', nombre.value);
        formData.append('correo', correo.value);
        formData.append('foto', document.getElementById('foto').files[0]);
        formData.append('contrasenia', contrasenia.value);

        fetch(URL + 'usuarios', {
                method: 'POST',
                body: formData
            })
            .then(function (response) {
                if (response.ok) {
                    return response.json();
                }
            })
            .then(function (data) {
                alert('Usuario agregado correctamente.');
                // Limpiar el formulario para el próximo usuario
                nombre.value = "";
                correo.value = "";
                document.getElementById('foto').value = "";
                contrasenia.value = "";
                parrafo.innerHTML = ""; // Limpiar cualquier mensaje de advertencia
            })
            .catch(function (error) {
                alert('El usuario ya existe');
                
            });
    }
});

