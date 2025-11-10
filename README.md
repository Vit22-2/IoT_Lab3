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

- Open **Thonny IDE** and connect your **ESP32** board.  
- Upload the following files to the ESP32:
   - `bmp280.py` → BMP280 driver  
   - `main.py` → Main program (choose MQTT or ThingsBoard version)  
- Make sure both files appear in the **device sidebar** in Thonny.
- Click Run in Thonny to execute the code.  
- Watch the output to see:
   - Temperature (°C)  
   - Pressure (hPa)  
   - Altitude (m)  
- Verify that the ESP32 connects to your Wi-Fi successfully.
- Open **[MQTT Explorer](https://github.com/thomasnordquist/MQTT-Explorer/releases/tag/v0.4.0-beta.6)**.  
- Connect to the thingsbooard dashboard.
