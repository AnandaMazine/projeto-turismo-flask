from flask import Flask
from flasgger import Swagger
import os
from dotenv import load_dotenv
from .database import init_db, db

# SCHEMAS
from .schemas.destination_schema import DestinationSchema
from .schemas.hotel_schema import HotelSchema
from .schemas.tour_schema import TourSchema
from .schemas.booking_schema import BookingSchema

load_dotenv()

def create_app():
    app = Flask(__name__)
    init_db(app)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Turismo",
            "description": "API para gestão de viagens e reservas",
            "version": "1.0.0"
        },
        "definitions": {
            "Destination": DestinationSchema.model_json_schema(),
            "Hotel": HotelSchema.model_json_schema(),
            "Tour": TourSchema.model_json_schema(),
            "Booking": BookingSchema.model_json_schema(),
            "Error": {
                "type": "object",
                "properties": {"error": {"type": "string"}}
            }
        }
    }

    Swagger(app, template=swagger_template)

    from .routes.destinations import destinations_bp
    from .routes.hotels import hotels_bp
    from .routes.tours import tours_bp
    from .routes.bookings import bookings_bp

    app.register_blueprint(destinations_bp)
    app.register_blueprint(hotels_bp)
    app.register_blueprint(tours_bp)
    app.register_blueprint(bookings_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)