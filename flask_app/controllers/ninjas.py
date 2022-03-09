from flask import render_template, request, redirect 
from flask_app import app
from flask_app.models import ninja, dojo


@app.route('/ninjas/new')
def index():
    return render_template('new_ninja.html', dojos=dojo.Dojo.get_all())    

@app.route("/ninjas/create", methods=["POST"])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/dojos')    