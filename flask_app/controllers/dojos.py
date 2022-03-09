from flask import render_template, request, redirect 
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def main():
    return render_template('new_dojo.html', dojos = Dojo.get_all())

@app.route('/dojos/new', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')                           
def show(id):
    data ={
        "id": id
    }
    return render_template("show_dojo.html", dojo=Dojo.get_all_ninjas(data))


# @app.route('/dojos/show')
# def direct():
#     return redirect('/dojos/show/<int:id>')