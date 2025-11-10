# main.py — ESP32 + BMP280 → ThingsBoard Cloud (MQTT)
import network, time, json
from umqtt.simple import MQTTClient
from machine import Pin, I2C
from bmp280 import BMP280

# ---------- Wi-Fi ----------
SSID = "Robotic WIFI"
PASS = "rbtWIFI@2025"

# ---------- ThingsBoard Cloud ----------
TB_HOST = "mqtt.thingsboard.cloud"
TB_PORT = 1883
TB_TOKEN = b"wAyWZtDndBn7z9tZMdZ1"   # <-- PUT YOUR TOKEN HERE
TOPIC   = b"v1/devices/me/telemetry"

# ---------- Wi-Fi Connection ----------
w = network.WLAN(network.STA_IF)
w.active(True)
if not w.isconnected():
    print("Connecting to Wi-Fi...")
    w.connect(SSID, PASS)
    t0 = time.ticks_ms()
    while not w.isconnected():
        if time.ticks_diff(time.ticks_ms(), t0) > 15000:
            raise RuntimeError("Wi-Fi connection timeout")
        time.sleep(0.3)
print("✅ Wi-Fi connected:", w.ifconfig())

# ---------- MQTT Connection ----------
client = MQTTClient(
    client_id=b"esp32-tb",
    server=TB_HOST,
    port=TB_PORT,
    user=TB_TOKEN,   # <--- your device token here
    password=b"",
    keepalive=30,
    ssl=False
)
client.connect()
print("✅ Connected to ThingsBoard Cloud")

# ---------- BMP280 Sensor Setup ----------
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
bmp = BMP280(i2c, addr=0x76)
print("✅ BMP280 sensor ready")

# ---------- Loop: Read sensor + Publish ----------
while True:
    temp = round(bmp.temperature, 2)
    pres = round(bmp.pressure / 100, 2)   # convert Pa → hPa
    alt  = round(bmp.altitude, 2)

    payload = {
        "temperature": temp,
        "pressure": pres,
        "altitude": alt
    }

    msg = json.dumps(payload)
    print("Publishing:", msg)

    try:
        client.publish(TOPIC, msg)
        print("✅ Data sent to ThingsBoard\n")
    except Exception as e:
        print("⚠️ Publish failed:", e)

    time.sleep(5)
