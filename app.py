from flask import Flask, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print(f"Error loading the model: {e}")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array(data['features'])
        prediction = model.predict(features.reshape(1, -1))
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
