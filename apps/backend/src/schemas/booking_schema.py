from pydantic import BaseModel

class BookingSchema(BaseModel):
    id: int | None = None
    hospede: str
    hotel_id: int
    data_reserva: str
    valor_total: float
    status: str