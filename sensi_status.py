import requests

# Replace with your Home Assistant details
HA_URL = "http://<HOME_ASSISTANT_IP>:8123"
ENTITY_ID = "climate.sensi"
TOKEN = "YOUR_LONG_LIVED_ACCESS_TOKEN"

def get_sensi_data():
    try:
        url = f"{HA_URL}/api/states/{ENTITY_ID}"
        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        return {
            "mode": data['attributes'].get('hvac_mode', 'unknown'),
            "temp": data['attributes'].get('current_temperature', 'N/A'),
            "target": data['attributes'].get('temperature', 'N/A')
        }

    except Exception as e:
        print("❌ Error fetching Sensi thermostat data:", e)
        return {
            "mode": "Error",
            "temp": "N/A",
            "target": "N/A"
        }


