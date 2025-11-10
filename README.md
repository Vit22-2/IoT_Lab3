# IoT_Lab3

## Features

- Read **temperature**, **pressure**, and **altitude** from the **BMP280** sensor  
- Display live readings in **Thonny**  
- Publish sensor or random data to an **MQTT broker** (e.g., `test.mosquitto.org`)  
- Connect to **ThingsBoard Cloud** to send live IoT telemetry  
- Visualize real-time data on a **ThingsBoard Dashboard**  
- Demonstrate full IoT workflow: **Sensor → ESP32 → MQTT → Cloud Dashboard**

## Requirements

### Hardware
- ESP32 (MicroPython firmware installed)  
- BMP280 Sensor (I²C mode)  
- Breadboard + Jumper Wires  
- USB Cable + Laptop  
- Stable Wi-Fi connection  

### Software
- [Thonny IDE](https://thonny.org/)  
- MicroPython firmware uploaded to ESP32  
- `bmp280.py` driver file saved to ESP32  
- [MQTT Explorer](https://github.com/thomasnordquist/MQTT-Explorer/releases/tag/v0.4.0-beta.6) (optional for monitoring MQTT)

## Wiring

<img width="1602" height="847" alt="image" src="https://github.com/user-attachments/assets/e0c4b477-2dc7-4d45-b7c6-955aa09b8233" />

## Usage Instructions

- Upload Files to ESP32
  - In Thonny, open and upload bmp280.py and lab3.py to the ESP32.
  - Run the Code
  - The Thonny Shell will show live temperature, pressure, and altitude values.
- MQTT Testing
  - Open MQTT Explorer, connect to test.mosquitto.org, and search your topic (e.g. aupp/lab/random). You’ll see data published every 5 seconds.
- ThingsBoard Cloud Dashboard
  - Log in to ThingsBoard Cloud
  - Open your device and check Latest Telemetry
  - Create a dashboard widget (e.g., gauge or chart) to visualize the values.
- Use BMP280 readings for live environment monitoring.

## Screenshots of MQTT and Thingsboard

## Short demo video (60–90s)
