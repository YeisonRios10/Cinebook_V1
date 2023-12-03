from flask import render_template

def configure_routes(app):
    # Configurar rutas generales
    @app.route('/')
    def index():
        return render_template('dashboard.html')