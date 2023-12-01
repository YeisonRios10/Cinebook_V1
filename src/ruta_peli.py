from flask import render_template

def configure_routes(app):
    @app.route('/alicia_peli')
    def alicia_peli():
        return render_template('pelicula_alicia.html')
    
    @app.route('/harry_peli')
    def harry_peli():
        return render_template('pelicula_harry.html')
    
    @app.route('/it_peli')
    def it_peli():
        return render_template('pelicula_it.html')
    
    @app.route('/juegos_peli')
    def juegos_peli():
        return render_template('pelicula_juegos_hambre.html')
    
    @app.route('/leyenda_peli')
    def leyenda_peli():
        return render_template('pelicula_leyenda.html')
    
    @app.route('/lord_peli')
    def lord_peli():
        return render_template('pelicula_señor_anillos.html')
    
    @app.route('/maze_peli')
    def maze_peli():
        return render_template('pelicula_maze_runner.html')
    
    @app.route('/matilda_peli')
    def matilda_peli():
        return render_template('pelicula_matilda.html')