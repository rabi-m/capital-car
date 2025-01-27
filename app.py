from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# بيانات افتراضية
cars = [
    {"id": 1, "brand": "Tesla", "model": "Model S", "price": 75000},
    {"id": 2, "brand": "BMW", "model": "i8", "price": 120000},
    {"id": 3, "brand": "Audi", "model": "A6", "price": 55000},
]

@app.route("/")
def home():
    return render_template("index.html", cars=cars)

@app.route("/api/cars", methods=["GET", "POST"])
def car_api():
    if request.method == "POST":
        new_car = request.json
        cars.append(new_car)
        return jsonify({"message": "Car added successfully!", "car": new_car}), 201
    return jsonify(cars)

if __name__ == "__main__":
    app.run(debug=True)
