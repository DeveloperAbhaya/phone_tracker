# your_script.py
import phonenumbers
from main import number  # Make sure this import is correct

from phonenumbers import geocoder

# Parse the phone number
ch_number = phonenumbers.parse(number, "CH")

# Get the description for the phone number
print(geocoder.description_for_number(ch_number, "en"))

