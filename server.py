from flask_app import app
import flask_app.controllers.ninjas
import flask_app.controllers.dojos


if __name__=="__main__":
    app.run(debug=True)  