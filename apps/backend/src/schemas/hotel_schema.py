from pydantic import BaseModel

class HotelSchema(BaseModel):
    id: int | None = None
    nome_hotel: str
    estrelas: int
    valor_diaria: float
    cidade: str