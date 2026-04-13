from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

#definir la aplicacion
app = Flask(__name__)

# definir variables 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contactos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '454ghgghfg8h9fghjnrjtr'

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
    num_contactos=0
    print(request)
    if request.method == "POST":
        nombre =request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        
      
        
        if len(nombre) < 3:
            return "El nombre debe tener al menos 3 caracteres"
        
        if len(telefono) < 1:
            return "ingresar un numero"
        
        if contacto.query.filter_by(correo=correo).first():
            return "este correo ya esta vinculado a otro usuaio"
        
        nuevo_contacto = contacto(
            nombre=nombre,
            correo = correo,
            telefono = telefono            
        )
        
    
        
        db.session.add(nuevo_contacto)
        db.session.commit()
        #return (f'contacto {nombre, correo, telefono} GUARDADO')
        

    return render_template("agregar_contactos.html")
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_contactos(id):
    cnt = contacto.query.get_or_404(id)
    if request.method == "POST":
        cnt.nombre = request.form["nombre"]
        cnt.correo = request.form["correo"]
        cnt.telefono = request.form["telefono"]
        
        db.session.commit()
        
    return render_template("editar_contacto.html", contacto=cnt)

@app.route ("/eliminar/<int:id>")
def eliminar_contactos(id):
    cnt = contacto.query.get_or_404(id)

    db.session.delete(cnt)
    db.session.commit()

    flash("Contacto eliminado correctamente", "success")
    return render_template("cnt_eliminado.html")
#iniciamos la aplicacion
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
