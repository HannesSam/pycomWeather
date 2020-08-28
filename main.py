import machine
from machine import Pin
from machine import I2C
import time
import pycom
import ubi #ubidots
import bme280_float as bme280

sleepTime = 900 # 15 minutes in seconds

i2c = machine.I2C() # This works as long as you connect to the defult connections for IC2 on pycom devices
# and that is P9 = SDA, P10 = scl
bme = bme280.BME280(i2c=i2c)


while True:

    adc = machine.ADC()             # create an ADC object
    apin = adc.channel(pin='P13')   # create an analog pin on P16
    millivolts = apin.voltage()     # Gets the voltage from that pin
    degC = (millivolts - 500.0) / 10.0 # Converts to Celsius according to the specifications for the sensor

    values = read_compensated_data() # Reads the data from the BME280

    ubi.post_var("pycomWeather", values[0], values[1], values[2], degC ) # Post the data to Ubidot

    time.sleep(sleepTime)
