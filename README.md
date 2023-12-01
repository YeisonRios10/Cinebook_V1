# Bibliocinefilos

## Requerimientos 

-  blinker==1.7.0
-  cffi==1.16.0
-  click==8.1.7
-  colorama==0.4.6
-  cryptography==41.0.7
-  Flask==3.0.0
-  Flask-Cors==4.0.0
-  Flask-MySQL==1.5.2
-  itsdangerous==2.1.2
-  Jinja2==3.1.2
-  MarkupSafe==2.1.3
-  mysql-connector-python==8.2.0
-  protobuf==4.21.12
-  pycparser==2.21
-  PyMySQL==1.1.0
-  Werkzeug==3.0.1


## Configuración del Entorno Local

Para ejecutar esta aplicación en tu entorno local, sigue estos pasos:

### 1. Clona el Repositorio

Clona este repositorio en tu máquina local utilizando Git:

```bash
git clone https://github.com/YeisonRios10/Cinebook_V1.git
```

### 2. Crea un entorno virtual

Muevete a la carpeta usuarios y ejecuta:

```bash
py -3 -m venv venv
```

### 3. Levanta el entorno virtual

Levanta el entorno virtual:

```bash
./venv/Scripts/activate
```

### 3. Instala las dependencias

Dentro del entorno virtual instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 4. Levanta la aplicacion

Ejecuta e ingresa en la dirección  http://127.0.0.1:5000