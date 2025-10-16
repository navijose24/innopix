import requests

def send_fine_notification(phone_number, vehicle_number, amount):
    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        "authorization": "g6Y18imray2wOR8fXHfbJjX2nKBHkZyOFDvkmsxie8xcrNK9xeEArizWanuJ",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "message": f"Alert! A fine of ₹{amount} has been issued for vehicle {vehicle_number}. Please pay it as soon as possible.",
        "language": "english",
        "route": "v3",
        "numbers": phone_number  # Ensure this is a string
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        print(f"SMS Response: {response.json()}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")