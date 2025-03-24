# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Collects data from BME680 sensor 
# and PM25 Sensor and creates a Table for it
"""
Example sketch to connect to PM2.5 sensor with either I2C or UART.
"""

# pylint: disable=unused-import
import time
import board
import busio
import sys
import csv
import adafruit_bme680
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25

reset_pin = None
# If you have a GPIO, its not a bad idea to connect it to the RESET pin
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direcimport boardtion = Direction.OUTPUT
# reset_pin.value = False


# For use with a computer running Windows:
# import serial
# uart = serial.Serial("COM30", baudrate=9600, timeout=1)

# For use with microcontroller board:
# (Connect the sensor TX pin to the board/computer RX pin)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
import board
# For use with USB-to-serial cable:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensobme680.sea_level_pressure = 1013.25bme680.sea_level_pressure = 1013.25r over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)


print(time.time())
file = open('davis.csv','w',newline = None)
csvwriter = csv.writer(file,delimiter=',')
# csvwriter.writerow(["Time", "Temp (C)", "Gas (Ohm)", "Humidity (%)", "PM 1.0: %d","PM 2.5: %d","PM 10: %d","Particles > 0.3um / 0.1L air", "Particles > 0.5um / 0.1L air","Particles > 1.0um / 0.1L air","Particles > 2.5um / 0.1L air","Particles > 5.0um / 0.1L air","Particles > 10um / 0.1L air"])
csvwriter.writerow(["Time", "Temp (C)", "Gas (Ohm)", "Humidity (%)", "PM 1.0: %d","PM 2.5: %d","PM 10: %d"])
print(sys.argv)
seconds_agrv = float(sys.argv[1])

i=0
time.sleep(6*60)
while i < seconds_agrv:
    time.sleep(1)
    Time = time.time()
    i += 1
    aqdata = pm25.read()
    # Code for checking for runtime error
    # print(aqdata)
    #    except RuntimeError:
    #   print("Unable to read from sensor, retrying...")
    #  continue
    csvwriter.writerow([Time,bme680.temperature,bme680.gas,bme680.relative_humidity, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]])
print("Ended loop")
file.close()




# Unused extraneous code
# print("Starting sensor readings at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#while i<5:
   # current_time = datetime.now().strftime("%H:%M:%S")
   # print(f"[{current_time}] Temp: {bme680.temperature:.1f} C, Gas: {bme680.gas} ohm," f"Humidity: {bme680.relative_humidity:.1f}%")
   # i+=1
  #  time.sleep(2)
# print("completed")

