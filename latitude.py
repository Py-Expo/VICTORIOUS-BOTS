import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Function to get location (latitude and longitude) for a phone number
def get_location(phone_number):
    # Parse the phone number string to convert it into phone number format
    phoneNumber = phonenumbers.parse(phone_number)
    
    # Storing the API Key in the Key variable
    Key = "f4b67186e3be43cdbf62b82a3d4ff7dd"  # Your OpenCage Geocode API key

    # Using the geocoder module of phonenumbers to get the location description
    location = geocoder.description_for_number(phoneNumber, "en")

    # Using the carrier module of phonenumbers to get the service provider name
    yourServiceProvider = carrier.name_for_number(phoneNumber, "en")

    # Using OpenCage to get the latitude and longitude of the location
    geocode = OpenCageGeocode(Key)
    query = f"{location}, {phoneNumber.country_code}"
    results = geocode.geocode(query)

    # Check if results are obtained
    if results and len(results):
        # Extracting latitude and longitude from the first result
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return {"phone_number": phone_number, "latitude": lat, "longitude": lng}
    else:
        # If latitude and longitude data are not available, return None
        return None

# Example list of phone numbers obtained from the backend
phone_numbers = ["+918489822747", "+917897896465", "+918596475623"]

# List to store the location data for each phone number
locations = []

# Iterate over the list of phone numbers
for number in phone_numbers:
    # Get the location data for the current phone number
    location_data = get_location(number)
    
    # If location data is available, append it to the list of locations
    if location_data:
        locations.append(location_data)

# Print the list of locations
for location in locations:
   print(location)