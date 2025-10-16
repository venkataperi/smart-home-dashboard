from flask import Flask, render_template
from sensor_reader import read_dht11
from weather_fetcher import get_weather
from blink_camera import fetch_and_save_latest_image
from detect_objects import run_detection
from sensi_status import get_sensi_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    temp, humidity = read_dht11()
    weather = get_weather()
    fetch_and_save_latest_image()
    detection_result = run_detection("static/latest.jpg")
    sensi = get_sensi_data()

    return render_template("index.html", temp=temp, humidity=humidity,
                           weather=weather, detection_result=detection_result,
                           sensi=sensi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



