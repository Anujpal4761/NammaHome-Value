from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# 🔥 Load artifacts when the app starts
print("Starting Flask server... Loading artifacts")
util.load_saved_artifacts()  # Ensure artifacts are loaded

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_locations_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Flask app is running...")
    app.run(debug=True)  # Debug mode to see errors
