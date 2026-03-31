import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from database import db
from models import Destination, Hotel

DESTINOS = [
    {"id": 1, "nome": "Iporanga", "cidade": "Iporanga", "estado": "SP", "pais": "Brasil"},
    {"id": 2, "nome": "Lençóis Maranhenses", "cidade": "Barreirinhas", "estado": "MA", "pais": "Brasil"}
]

HOTEIS = [
    {"id": 1, "nome_hotel": "Eco Pousada Beira Rio", "estrelas": 4, "valor_diaria": 350.0, "cidade": "Iporanga"},
    {"id": 2, "nome_hotel": "Porto Preguiças Resort", "estrelas": 5, "valor_diaria": 890.0, "cidade": "Barreirinhas"}
]

def seed():
    app = create_app()
    with app.app_context():
        if Destination.query.first():
            print("Banco já populado!")
            return

        print("Inserindo dados de turismo...")
        for d in DESTINOS:
            db.session.add(Destination(**d))
        
        for h in HOTEIS:
            db.session.add(Hotel(**h))
            
        db.session.commit()
        print("Seed finalizado com sucesso!")

if __name__ == '__main__':
    seed()