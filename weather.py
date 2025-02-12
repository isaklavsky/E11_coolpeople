import adafruit_bme680
print("Hello World")

import time
import board

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

run_duration = 10
starti_time = time.time()
i=0

print("Starting sensor readings at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

while i<5:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Temp: {bme680.temperature:.1f} C, Gas: {bme680.gas} ohm," f"Humidity: {bme680.relative_humidity:.1f}%")
    i+=1
    time.sleep(2)
print("completed")
