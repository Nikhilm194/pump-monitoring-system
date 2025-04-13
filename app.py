from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from pymodbus.client import ModbusTcpClient
import requests
from datetime import datetime
import random
import time

app = Flask(__name__)
CORS(app)

MODBUS_IP = '192.168.0.103'
MODBUS_PORT = 502
API_BASE = 'http://192.168.0.103:5001'

modbus_client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)

# Historical data storage
historical_data = {
    "timestamps": [],
    "water_pump": [],
    "lime_pump": [],
    "max_points": 20
}

def fetch_pump_data():
    try:
        now = datetime.now().strftime("%H:%M:%S")
        
        # Simulated data generation
        water_value = random.randint(0, 100)
        lime_value = random.randint(0, 100)
        
        # Update historical data
        historical_data['timestamps'].append(now)
        historical_data['water_pump'].append(water_value)
        historical_data['lime_pump'].append(lime_value)
        
        # Maintain data window
        for key in ['timestamps', 'water_pump', 'lime_pump']:
            if len(historical_data[key]) > historical_data['max_points']:
                historical_data[key].pop(0)
                
        return True
    except Exception as e:
        print(f"Data error: {str(e)}")
        return False

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/device_states')
def get_device_states():
    try:
        # Simulated device states
        return jsonify({
            "Pump1": random.choice([0, 1]),
            "Pump2": random.choice([0, 1]),
            "Pump3": random.choice([0, 1])
        })
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/pump_data')
def get_pump_data():
    if fetch_pump_data():
        return jsonify({
            "timestamps": historical_data['timestamps'],
            "datasets": [
                {"label": "Water Pump", "data": historical_data['water_pump']},
                {"label": "Lime Pump", "data": historical_data['lime_pump']}
            ]
        })
    return jsonify({"error": "Data fetch failed"}), 500

@app.route('/api/toggle/<pump_id>', methods=['POST'])
def toggle_pump(pump_id):
    try:
        return jsonify(
            success=True,
            message=f"Pump {pump_id} toggled (simulated)"
        )
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route('/api/reset', methods=['POST'])
def reset():
    try:
        historical_data.update({
            "timestamps": [],
            "water_pump": [],
            "lime_pump": []
        })
        return jsonify(success=True, message="System reset")
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
