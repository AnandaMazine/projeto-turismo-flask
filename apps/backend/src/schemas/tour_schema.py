from pydantic import BaseModel

class TourSchema(BaseModel):
    id: int
    nome_passeio: str
    duracao: str
    preco: float
    dificuldade: str