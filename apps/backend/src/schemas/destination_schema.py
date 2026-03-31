from pydantic import BaseModel

class DestinationSchema(BaseModel):
    id: int
    nome: str
    cidade: str
    estado: str