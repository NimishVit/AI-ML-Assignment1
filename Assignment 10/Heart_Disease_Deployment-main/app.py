from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        features = pd.DataFrame([data])
        
        prediction_value = model.predict(features)[0]
        
        # Formatting the response
        if prediction_value == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease Detected"
            
        # The API returns the prediction as JSON
        return jsonify({"prediction": result})
        
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)