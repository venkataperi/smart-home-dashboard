import Adafruit_DHT

def read_dht11():
    # Set the sensor type (DHT11)
    sensor = Adafruit_DHT.DHT11

    # GPIO pin connected to the DHT11 data pin (use 4 for GPIO4)
    pin = 4

    # Read humidity and temperature
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Round and return the values
    if humidity is not None and temperature is not None:
        return round(temperature, 1), round(humidity, 1)
    else:
        return None, None


