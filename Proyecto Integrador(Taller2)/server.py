<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, render_template, request, redirect, flash
>>>>>>> df9913e (Subiendo carpeta Proyecto Integrador al repositorio)
from pymongo import MongoClient
from flask_cors import CORS

# Configuración de Flask
app = Flask(__name__)
<<<<<<< HEAD
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

=======
app.secret_key = "secreto_seguro"
CORS(app)

# Conectar con MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["shoppingDB"]
    print("✅ Conectado a MongoDB correctamente.")
except Exception as e:
    print("❌ Error al conectar a MongoDB:", e)

# 📌 Ruta principal (Historial de compras y pujas)
@app.route('/')
def index():
    purchases = list(db.purchases.find({}, {"_id": 0}))
    bids = list(db.bids.find({}, {"_id": 0}))

    return render_template("index.html", purchases=purchases, bids=bids)

# 📌 Ruta de administración (Gestión de ofertas)
@app.route('/admin')
def admin():
    bids = list(db.bids.find({}, {"_id": 0}))  # Obtener todas las ofertas
    pending_bids = list(db.bids.find({"status": "Pendiente"}, {"_id": 0}))  # Obtener solo las pendientes

    return render_template("admin.html", bids=bids, pending_bids=pending_bids)

# 📌 Ruta para actualizar el estado de una oferta
@app.route('/update_status', methods=['POST'])
def update_status():
    auction_id = request.form.get('auctionId').strip()
    new_status = request.form.get('status').strip()

    if not auction_id or not new_status:
        flash("⚠ Error: Datos inválidos enviados.", "error")
        return redirect('/admin')

    # Actualizar todas las pujas con el mismo auctionId
    result = db.bids.update_many({"auctionId": auction_id}, {"$set": {"status": new_status}})

    if result.modified_count > 0:
        flash(f"✅ {result.modified_count} oferta(s) actualizada(s) a '{new_status}'", "success")
    else:
        flash(f"⚠ No se realizó ninguna actualización para {auction_id}.", "error")

    return redirect('/admin')

# Ejecutar la aplicación
>>>>>>> df9913e (Subiendo carpeta Proyecto Integrador al repositorio)
if __name__ == '__main__':
    app.run(debug=True)
