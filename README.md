# 🏡 Smart Home Dashboard (Raspberry Pi + Python + Flask)

A smart home monitoring and control system built with Python, Flask, and Raspberry Pi. This dashboard integrates multiple smart devices and sensors into a single, browser-accessible interface.

---

## 🚀 Features

- 🌡️ **DHT11 Sensor**: Read real-time indoor temperature & humidity
- 🌤️ **OpenWeatherMap API**: Fetch current outdoor weather forecast
- 🔌 **TP-Link Kasa Smart Devices**: Control plugs/lights over Wi-Fi
- 📷 **Blink Outdoor Camera**: Capture image + detect objects/people
- 🌡️ **Sensi Thermostat**: Display room temperature and HVAC status via Home Assistant
- 📊 **Flask Dashboard UI**: View everything in one browser-based dashboard

---

## 📷 Demo Screenshot

*(Add a screenshot of your dashboard UI here once available)*

---

## 🛠️ Technologies Used

| Tech              | Purpose                              |
|------------------|--------------------------------------|
| Python 3          | Core language                        |
| Flask             | Web framework                        |
| Adafruit DHT      | DHT11 GPIO sensor reading            |
| Requests          | API calls (Weather, Home Assistant)  |
| Blinkpy           | Blink camera cloud access            |
| Python-Kasa       | Kasa smart device control            |
| Jetson Inference  | Object/person detection (Jetson only)|
| Home Assistant    | Sensi thermostat integration         |

---

## 📦 Folder Structure


# smart-home-dashboard
Python-based Raspberry Pi dashboard for controlling smart devices (Kasa, Blink, Sensi) and sensors (DHT11)
