from pydantic import BaseModel

class DestinationSchema(BaseModel):
    id: int | None = None
    nome: str
    cidade: str
    estado: str