from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access backend

@app.route('/api/sensor-data')
def sensor_data():
    data = [
        {
            "name": "Vand dunk 1",
            "percentage": 15,
            "weight": 3
        },
        {
            "name": "Vand dunk 2",
            "percentage": 25,
            "weight": 5
        },
        {
            "name": "Vand dunk 3",
            "percentage": 75,
            "weight": 15
        },
        {
            "name": "Vand dunk 4",
            "percentage": 45,
            "weight": 9
        }
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
