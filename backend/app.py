from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access backend

@app.route('/api/sensor-data')
def sensor_data():
    data = [
        {
            "name": "Vand dunk 1",
            "percentage": 5,
            "weight": 0.5
        },
        {
            "name": "Vand dunk 2",
            "percentage": 90,
            "weight": 18
        },
        {
            "name": "Vand dunk 3",
            "percentage": 75,
            "weight": 15
        },
        {
            "name": "Vand dunk 4",
            "percentage": 50,
            "weight": 10
        }
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
