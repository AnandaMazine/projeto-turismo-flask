from pydantic import BaseModel

class TourSchema(BaseModel):
    id: int | None = None
    nome_passeio: str
    duracao: str
    preco: float
    dificuldade: str