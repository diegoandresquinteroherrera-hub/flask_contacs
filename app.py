from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#definir la aplicacion
app = Flask(__name__)

# definir variables 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contactos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(20))
# definimos ruta y template
@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/contactos")
def contactos():
    
    lista_contactos = contacto.query.all()
    lista_ordenada = sorted(lista_contactos, key =lambda contacto : contacto.nombre)
    return render_template("contactos.html", contactos = lista_ordenada)

@app.route("/agregar", methods=["GET", "POST"])
def agregar_contactos():
    
    print(request)
    if request.method == "POST":
        nombre =request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        
        if len(nombre) < 3:
            return "El nombre debe tener al menos 3 caracteres"
        
        if len(telefono) < 1:
            return "ingresar un numero"
        
        nuevo_contacto = contacto(
            nombre=nombre,
            correo = correo,
            telefono = telefono            
        )
        
        db.session.add(nuevo_contacto)
        db.session.commit()
        
        #return (f'contacto {nombre, correo, telefono} GUARDADO')
    
        

    return render_template("agregar_contactos.html")

#iniciamos la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
    
    
with app.app_context():
    db.create_all()