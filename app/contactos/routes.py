from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import Contacto
from .. import db

contactos_bp = Blueprint("contactos", __name__)

home_bp= Blueprint("/contactos", __name__)

@contactos_bp.route("/")
def inicio():
    return render_template("index.html")

@contactos_bp.route("/contactos")
def contactos():
    
    lista_contactos = Contacto.query.all()
    return render_template("contactos.html", contactos=lista_contactos)

@contactos_bp.route("/agregar", methods=["GET", "POST"])
def agregar_contacto():
    
    if request.method == "POST":
        
        nombre =request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        
      
        
        if len(nombre) < 3:
            return "El nombre debe tener al menos 3 caracteres"
        
        if len(telefono) < 1:
            return "ingresar un numero"
        
        if Contacto.query.filter_by(correo=correo).first():
            return "este correo ya esta vinculado a otro usuaio"
        
        nuevo = Contacto(
            nombre=request.form["nombre"],
            correo=request.form["correo"],
            telefono=request.form["telefono"]
            
        )
        
        db.session.add(nuevo)
        db.session.commit()
        
       
    return render_template("agregar_contactos.html")

@contactos_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_contacto(id):
    
    contacto = Contacto.query.get_or_404(id)
    
    if request.method == "POST":
        contacto.nombre = request.form["nombre"],
        contacto.correo = request.form["correo"],
        contacto.telefono = request.form["telefono"]
        
        db.session.commit()
        
        return redirect(url_for("contactos.contactos"))
    
    return render_template("editar_contacto.html", contacto=contacto)

@contactos_bp.route("/eliminar/<int:id>")
def eliminar_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    
    db.session.delete(contacto)
    db.session.commit()
    flash("Contacto eliminado correctamente", "success")
    
    return redirect(url_for("contactos.contactos"))
