from pydantic import BaseModel

class HotelSchema(BaseModel):
    id: int
    nome_hotel: str
    estrelas: int
    valor_diaria: float
    cidade: str