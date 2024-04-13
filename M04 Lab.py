
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.module):
    id = db.Column(db.Interger, primary_key = True)
    name =  db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name}-{self.description}"
    
    @app.route('/')

    def home():
        return 'Hello!'
    
    @app.route('/drinks')
    def get_drinks():
        drinks = Drink.query.all()
        print([drink.id for drink in drinks])
        return jsonify({"drinks": [{"name": drink.name, "description": drink.description} for drink in drinks]})
    
    @app.route('/drinks/<id>')
    def get_drinks(id):
        drinks = Drink.query.get_404(id)
        print("see if drink:", drink.name)
        return {"name": drink.name, "description": drink.description}
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '_main_':
    app.run(debug = True)