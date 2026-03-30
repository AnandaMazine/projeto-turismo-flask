from flask import Flask
from flasgger import Swagger
from .routes.destinations import destinations_bp
from .routes.hotels import hotels_bp
from .routes.tours import tours_bp
from .routes.bookings import bookings_bp

def create_app():
    app = Flask(__name__)

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'Projeto Turismo Flask',
        'uiversion': 3
    }
    Swagger(app)

    app.register_blueprint(destinations_bp, url_prefix='/destinations')
    app.register_blueprint(hotels_bp, url_prefix='/hotels')
    app.register_blueprint(tours_bp, url_prefix='/tours')
    app.register_blueprint(bookings_bp, url_prefix='/bookings')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)