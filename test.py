import requests
import json

# Backend URL (Update if different)
backend_url = "http://127.0.0.1:8000/api/save-detection/"

# Sample data to send
data = {
    "vehicle_type": "Car",
    "number_plate": "KL06AA 7856",
    "waste_detected": True
}

# Send POST request to backend
response = requests.post(backend_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

# Print the response from the backend
print("Response Status Code:", response.status_code)
print("Response Data:", response.json())