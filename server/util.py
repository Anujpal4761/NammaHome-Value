import pickle
import json
import os
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    """Returns the estimated price based on input parameters."""
    if __model is None:
        print("Error: Model is not loaded. Call 'load_saved_artifacts()' first.")
        return None

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1  # If location is not found

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_locations_names():
    """Returns the list of location names if artifacts are loaded."""
    if __locations is None:
        print("Artifacts not loaded. Call 'load_saved_artifacts()' first.")
        return []
    return __locations


def get_data_columns():
    """Returns the full list of data columns."""
    if __data_columns is None:
        print("Artifacts not loaded. Call 'load_saved_artifacts()' first.")
        return []
    return __data_columns


def get_model():
    """Returns the loaded model."""
    if __model is None:
        print("Artifacts not loaded. Call 'load_saved_artifacts()' first.")
        return None
    return __model
def load_saved_artifacts():
    """Loads the trained model and column information."""
    print("🔄 Loading saved artifacts...")

    global __data_columns
    global __locations
    global __model

    artifacts_path = "./artifacts"

    # Load columns.json
    columns_path = os.path.join(artifacts_path, "columns.json")
    if not os.path.exists(columns_path):
        print(f"❌ Error: {columns_path} not found!")
        return

    with open(columns_path, 'r') as f:
        __data_columns = json.load(f).get("data_columns", [])

    print("📂 Loaded columns:", __data_columns)

    if len(__data_columns) > 3:
        __locations = [col.replace("location_", "") for col in __data_columns[3:]]
    else:
        print("⚠️ Warning: No locations found in data columns!")
        __locations = []

    print("📍 Extracted locations:", __locations)

    # Load model
    model_path = os.path.join(artifacts_path, "banglore_home_prices_model.pickle")
    if not os.path.exists(model_path):
        print(f"❌ Error: {model_path} not found!")
        return

    with open(model_path, 'rb') as f:
        __model = pickle.load(f)

    print("✅ Loading saved artifacts... Done!")


if __name__ == "__main__":
    load_saved_artifacts()
    print("Available locations:", get_locations_names())

    # Sample predictions
    locations_to_test = [
        ('1st Phase JP Nagar', 1000, 3, 3),
        ('1st Phase JP Nagar', 1000, 2, 2),
        ('Kalhalli', 1000, 2, 2),
        ('Ejipura', 1000, 2, 2)
    ]

    for loc, sqft, bhk, bath in locations_to_test:
        price = get_estimated_price(loc, sqft, bhk, bath)
        print(f"Estimated price for {loc} ({sqft} sqft, {bhk} BHK, {bath} Bath): {price}")
