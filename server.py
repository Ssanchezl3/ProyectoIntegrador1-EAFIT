from flask import Flask, render_template
from pymongo import MongoClient
from flask_cors import CORS

# Configuración de Flask
app = Flask(__name__)
CORS(app)  # Permitir acceso CORS

# Conexión con MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["shoppingDB"]

# Ruta para mostrar todos los datos combinados en una página HTML
@app.route('/', methods=['GET'])
def index():
    purchases = list(db.purchases.find({}, {"_id": 0}))
    bids = list(db.bids.find({}, {"_id": 0}))
    return render_template("index.html", purchases=purchases, bids=bids)

if __name__ == '__main__':
    app.run(debug=True)
