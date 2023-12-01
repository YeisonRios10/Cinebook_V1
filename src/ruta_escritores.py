from flask import render_template
 
def configure_routes(app):
    @app.route('/alicia')
    def alicia():
        return render_template('escritor_alicia.html')
    
    @app.route('/harry')
    def harry():
        return render_template('escritor_harry.html')
    
    @app.route('/it')
    def it():
        return render_template('escritor_it.html')
    
    @app.route('/juegos')
    def juegos():
        return render_template('escritor_juegos_del_hambre.html')
    
    @app.route('/leyenda')
    def leyenda():
        return render_template('escritor_soy_leyenda.html')
    
    @app.route('/lord')
    def lord():
        return render_template('escritor_señor_anillos.html')
    
    @app.route('/maze')
    def maze():
        return render_template('escritor_maze_runner.html')
    
    @app.route('/matilda')
    def matilda():
        return render_template('escritor_matilda.html')