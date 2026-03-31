from pydantic import BaseModel

class BookingSchema(BaseModel):
    id: int
    hospede: str
    hotel_id: int
    data_reserva: str
    valor_total: float
    status: str