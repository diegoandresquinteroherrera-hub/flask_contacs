from . import db
class Contacto(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(20))