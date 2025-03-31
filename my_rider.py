import googlemaps
import geocoder
from geopy.distance import geodesic
import sys

# Google Maps API Key (with my own)
GOOGLE_MAPS_API_KEY = "AIzaSyC687a_V30X-wp1assQbiFiO8JNvhuei54"

# Price per kilometer (Rwandan Francs)
PRICE_PER_KM = 100  

# Define Kigali city boundary (Latitude, Longitude)
KIGALI_BOUNDARIES = {
    "north": -1.885,
    "south": -2.030,
    "east": 30.195,
    "west": 29.991
}

# Initialize Google Maps API
gmaps = googlemaps.Client(key="AIzaSyC687a_V30X-wp1assQbiFiO8JNvhuei54")

def get_current_location():
    """ Get user's real-time GPS coordinates """
    g = geocoder.ip("me")  # Gets real-time location based on IP
    if g.latlng:
        return tuple(g.latlng)
    else:
        print("Could not detect your current location. Please enter it manually.")
        sys.exit(1)

def get_coordinates(location_name):
    """ Get latitude and longitude of a location using Google Maps API """
    try:
        location = gmaps.geocode(location_name + ", Kigali, Rwanda")
        if location:
            lat = location[0]["geometry"]["location"]["lat"]
            lon = location[0]["geometry"]["location"]["lng"]
            return (lat, lon)
        else:
            print(f"Could not find location: {location_name}. Please enter a valid area in Kigali.")
            sys.exit(1)
    except Exception as e:
        print(f"Error fetching location: {e}")
        sys.exit(1)

def is_within_kigali(coords):
    """ Check if coordinates are within Kigali boundaries """
    lat, lon = coords
    return (KIGALI_BOUNDARIES["south"] <= lat <= KIGALI_BOUNDARIES["north"] and
            KIGALI_BOUNDARIES["west"] <= lon <= KIGALI_BOUNDARIES["east"])

def calculate_cost(start_coords, end_coords):
    """ Calculate distance and cost within Kigali """
    if not (is_within_kigali(start_coords) and is_within_kigali(end_coords)):
        print("Error: One or both locations are outside Kigali. Please enter locations within Kigali.")
        sys.exit(1)
    
    # Calculate distance in km
    distance_km = geodesic(start_coords, end_coords).kilometers

    # Calculate total price
    total_cost = distance_km * PRICE_PER_KM
    
    return round(distance_km, 1), round(total_cost, 0)

if __name__ == "__main__":
    # Automatically detect user's current location
    print("Detecting your location...")
    start_coords = get_current_location()
    print(f"Your current location: {start_coords}")

    # User inputs destination
    end_location = input("Enter your destination in Kigali: ")
    end_coords = get_coordinates(end_location)

    # Calculate distance and cost
    distance, cost = calculate_cost(start_coords, end_coords)

    print(f"\nDistance: {distance} km")
    print(f"Estimated cost: {cost} RWF")
