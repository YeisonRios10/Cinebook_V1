from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import mysql.connector
from werkzeug.utils import secure_filename
import os
import time 
from rutas import configure_routes as configure_rutas
from ruta_peli import configure_routes as configure_ruta_peli
from ruta_escritores import configure_routes as configure_ruta_escritores

app = Flask(__name__, static_url_path='/static')
CORS(app)

configure_rutas(app)  # Integrar las rutas generales
configure_ruta_peli(app)  # Integrar las rutas específicas de Alicia
configure_ruta_escritores(app) 

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database  # Agregado: especifica la base de datos al conectar
        )
        self.cursor = self.conn.cursor(dictionary=True)

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
            id int not null auto_increment,
            nombre varchar(255),
            correo varchar(255),
            foto varchar(5000),
            contrasenia varchar(255),
            primary key(id))
                            ''')
        self.conn.commit()

    def agregar_usuario(self, nombre, correo, foto, contrasenia):
        self.cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        usuario_existe = self.cursor.fetchone()
        if usuario_existe:
            return False

        sql = "INSERT INTO usuarios (nombre, correo, foto, contrasenia) VALUES (%s, %s, %s, %s)"
        valores = (nombre, correo, foto, contrasenia)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True

    def consultar_usuario(self, id):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE id = {id}")
        return self.cursor.fetchone()
    
    def modificar_usuario(self, id, update_nombre, update_correo, update_foto, update_contrasenia):
        sql = "UPDATE usuarios SET nombre = %s, correo = %s, foto = %s, contrasenia = %s WHERE id = %s"
        valores = (update_nombre, update_correo, update_foto, update_contrasenia, id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcont > 0
    
    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios ORDER BY id")
        usuarios = self.cursor.fetchall()
        return usuarios 
    
    def eliminar_usuario(self, id):
        self.cursor.execute(f"DELETE FROM usuarios WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcont > 0
    
    def mostrar_usuario(self, id):
        usuario = self.consultar_usuario(id)
        if usuario:
            print("¨" * 40)
            print(f"Id........: {usuario['id']}")
            print(f"Nombre....: {usuario['nombre']}")
            print(f"Correo....: {usuario['correo']}")
            print(f"Foto......: {usuario['foto']}")
            print(f"Contraseña: {usuario['contrasenia']}")
            print("-" * 40)
        else:
            print("Usuario no encontrado.")
                
#Cuerpo del programa
catalogo = Catalogo(host='localhost', user='root', password='root', database='app')        
    
#catalogo.agregar_usuario(1, 'Kevin De Bruyne', 'debruyne@outlook.es', '17.jpg', '@debruyne17')
#catalogo.agregar_usuario(2, 'Karla Lopez','lopezk@outlook.es', 'karla.jpg','w@karla.o')

RUTA_DESTINO = './src/uploads/'

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = catalogo.listar_usuarios()
    return jsonify(usuarios)

@app.route("/usuarios/<int:id>", methods=["GET"])
def mostrar_usuario(id):
    usuario = catalogo.consultar_usuario(id)
    if usuario:
        return jsonify(usuario), 201
    else:
        return "Usuario no encontrado", 404

@app.route("/usuarios", methods=["POST"])
def agregar_usuario():
    #Recojo los datos del form
    nombre = request.form['nombre']
    correo = request.form['correo']
    foto = request.files['foto']
    contrasenia = request.form['contrasenia']  
    
    nombre_foto = secure_filename(foto.filename)
    nombre_base, extension = os.path.splitext(nombre_foto)
    nombre_foto = f" {nombre_base}_{int(time.time())}{extension}"
    
    #Guardar la imagen en la carpeta de destino
    ruta_destino = os.path.join(RUTA_DESTINO, nombre_foto)
    foto.save(ruta_destino)
    if catalogo.agregar_usuario(nombre, correo, nombre_foto, contrasenia):
        return jsonify({"mensaje": "Usuario agregado"}), 201
    else:
        return jsonify({"mensaje": "Usuario ya existe"}),400

    

@app.route("/usuarios/<int:id>", methods=["PUT"])
def modificar_usuario():
    #Recojo los datos del form
    update_nombre = request.form.get("nombre")
    update_correo = request.form.get("correo")
    up_foto = request.files['foto']
    update_contrasenia = request.form.get("contrasenia")
    
    # Procesamiento de la imagen
    nombre_foto = secure_filename(up_foto.filename)
    nombre_base, extension = os.path.splitext(nombre_foto)
    nombre_foto = f"{nombre_base}_{int(time.time())}{extension}"
    up_foto.save(os.path.join(RUTA_DESTINO, nombre_foto))
    
    usuario = catalogo.consultar_usuario(id)
    if usuario:
        foto_vieja = usuario["foto"]
        ruta_foto = os.path.join(RUTA_DESTINO, foto_vieja)
        
        if os.path.exists(ruta_foto):
            os.remove(ruta_foto)

    # Llamada a la función de modificar_usuario con los parámetros correctos
    if catalogo.modificar_usuario(id, update_nombre, update_correo, nombre_foto, update_contrasenia):
        return jsonify({"mensaje": "Usuario modificado"}), 200
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 403

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    # Busco el usuario guardado
    usuario = usuario = catalogo.consultar_usuario(id)
    if usuario: # Si existe el usuario...
        foto_vieja = usuario["foto"]
        # Armo la ruta a la imagen
        ruta_foto = os.path.join(RUTA_DESTINO, foto_vieja)

        # Y si existe la borro.
        if os.path.exists(ruta_foto):
            os.remove(ruta_foto)

    # Luego, elimina el usuario del catálogo
    if catalogo.eliminar_usuario(id):
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error al eliminar el usuario"}), 500



@app.route('/escritores')
def escritores(): 
    return render_template('escritores.html')

@app.route('/conocenos')
def conocenos():
    return render_template('conocenos.html')

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/listado')
def listado():
    return render_template('listado.html')

@app.route('/modificar')
def modificar():
    return render_template('modificaciones.html')

if __name__ == '__main__':
    app.run(debug=True)
    