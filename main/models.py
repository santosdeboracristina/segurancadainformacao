from main import db
from datetime import datetime

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11),nullable=False)
    prontuarios = db.relationship('Prontuario', backref='Paciente', lazy=True)

    def __repr__(self):
        return f"Paciente('{self.username}', '{self.email}', '{self.image_file}')"

class Prontuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    conteudo = db.Column(db.Text, nullable=False)
    prontuario_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
