from database import db

class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cidade = db.Column(db.String, nullable=False)
    estado = db.Column(db.String(2))
    pais = db.Column(db.String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    nome_hotel = db.Column(db.String, nullable=False)
    estrelas = db.Column(db.Integer)
    valor_diaria = db.Column(db.Float, nullable=False)
    cidade = db.Column(db.String, nullable=False)

    # Relacionamento: um hotel tem várias reservas
    bookings = db.relationship('Booking', backref='hotel', cascade='all, delete-orphan')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    nome_passeio = db.Column(db.String, nullable=False)
    duracao = db.Column(db.String)
    preco = db.Column(db.Float, nullable=False)
    dificuldade = db.Column(db.String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    hospede = db.Column(db.String, nullable=False)
    data_reserva = db.Column(db.String)
    valor_total = db.Column(db.Float)
    status = db.Column(db.String, default="Confirmada")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}