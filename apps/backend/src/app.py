from flask import Flask
from flasgger import Swagger
from routes.destinations_route import destinations_bp

def create_app():
    app = Flask(__name__)

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'Projeto Turismo Flask',
        'uiversion': 3
    }
    Swagger(app)

    # Espaço reservado para registrar Blueprints depois
    app.register_blueprint(destinations_bp, url_prefix='/destinations')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)