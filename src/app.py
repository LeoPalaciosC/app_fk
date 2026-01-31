from flask import Flask, request, render_template
import os
from joblib import load


from joblib import load
app = Flask(__name__)
# Cargar el modelo desde el archivo
model = load(open("../models/decision_tree_regressor_default_42.sav", "rb"))
print("✅ Modelo cargado exitosamente!")
        
        # Ejemplo de uso:
        # predictions = model.predict(X_new_data)
  


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])

        data = [[val1, val2, val3]]
        prediction = str(model.predict(data)[0])
        #pred_class = class_dict[prediction]
    else:
        prediction = None
    return render_template("index.html", prediction = prediction)
    
