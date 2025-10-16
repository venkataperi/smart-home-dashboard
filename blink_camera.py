from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
import requests
import os

# Replace with your Blink account credentials
USERNAME = "your_email@example.com"
PASSWORD = "your_password"

# Where to save the image (adjust path if needed)
SAVE_PATH = "static/latest.jpg"

def fetch_and_save_latest_image():
    try:
        blink = Blink()
        blink.auth = Auth({"username": USERNAME, "password": PASSWORD})
        blink.start()

        # Grab the camera object (adjust name if needed)
        camera = blink.cameras['Outdoor']

        # Get the image URL
        img_url = camera.image

        # Download the image
        img_data = requests.get(img_url).content

        # Save it to the static folder
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        with open(SAVE_PATH, "wb") as f:
            f.write(img_data)

        print("✅ Blink image saved:", SAVE_PATH)

    except Exception as e:
        print("❌ Error fetching image from Blink:", e)


