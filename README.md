🏠 Namma Home Price Predictor - Bangalore 
🧠💻🌐
A machine learning powered web application that predicts the price of a house in Bangalore based on area, location, BHK, and number of bathrooms.



🔧 Tech Stack
Machine Learning: Scikit-learn, Pandas, NumPy

Model Serialization: Pickle

Backend: Flask (REST API)

Frontend: HTML5, CSS3, JavaScript

Deployment Ready

💡 Features
Predicts house prices based on:

✅ Area in square feet

✅ Number of BHKs

✅ Number of Bathrooms

✅ Location

Clean and interactive UI

Backend API built using Flask

Easily extendable to other cities or more features

🚀 Preview
📷 Live Demo — (Add your deployed site URL here if available)

📁 Project Structure
.
├── artifacts/
│   ├── banglore_home_prices_model.pickle
│   └── columns.json
├── server/
│   ├── util.py
│   └── app.py
├── client/
│   ├── app.html
│   ├── app.css
│   └── app.js
├── model/
│   ├── data_cleaning.ipynb
│   └── model_training.ipynb
├── README.md

📦 Setup Instructions
.
├── artifacts/
│   ├── banglore_home_prices_model.pickle
│   └── columns.json
├── server/
│   ├── util.py
│   └── app.py
├── client/
│   ├── app.html
│   ├── app.css
│   └── app.js
├── model/
│   ├── data_cleaning.ipynb
│   └── model_training.ipynb
├── README.md

📦 Setup Instructions
  1. Clone the repo
     git clone https://github.com/Anujpal4761/NammaHome-Value/tree/main.git
     cd bangalore-house-price-predictor
  2. Install dependencies
     pip install -r requirements.txt
  3. Run the Flask server
     cd server
     python app.py
  4. Open app.html in browser Or serve via a simple web server for a better experience:
     cd client
     python -m http.server

📈 Machine Learning Details
 1. Linear Regression model trained on a dataset of Bangalore real estate listings
 2. One-hot encoding for locations
 3. Feature engineered columns: sqft, BHK, bath, and location   



