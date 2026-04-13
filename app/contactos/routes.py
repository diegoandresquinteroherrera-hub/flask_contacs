from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Contacto
from .. import db

contactos_bp = Blueprint("contactos", __name__)

@contactos_bp.route("/")
def contactos():
    
    lista_contactos = Contacto.query.all()
    return render_template("contactos.html", contacto=lista_contactos)

@contactos_bp.route("/agregar", methods["GET", "POST"])
def agregar_contacto():
    
    if request.method == "POST":
        
        nuevo = Contacto(
            nombre=request.form["nombre"],
            correo=request.form["correo"],
            telefono=request.form["telefono"]
            
        )
        
        db.session.add(nuevo)
        db.session.commit()
        
        return redirect(url_for("contactos.contactos"))
    return render_template("agregar_contacto.html")

@contactos_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_contacto(id):
    
    contacto = Contacto.query.get_or_404(id)
    
    if request.method == "POST":
        contacto.nombre = request.form["nombre"],
        contacto.correo = request.form["correo"],
        contacto.telefono = request.form["telefono"]
        
        db.session.commit()
        
        return redirect(url_for("contactos.contactos"))
    
    return render_template("edtitar_contacto.html", contacto=contacto)

@contactos_bp.route("/eliminar/<int:id>")
def eliminar_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    
    db.session.delete(contacto)
    db.session.commit()
    
    return redirect(url_for("contactos.contactos"))
