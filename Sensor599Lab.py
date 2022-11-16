#IMports
import bme680
import time
import os
from datetime import datetime

def main() :
    #repeat loop
    repeat = 2880
    #seconds between reading
    wait_period = 30
    #keep track
    count = 0

    #activate sensor
    sensor = bme680.BME680(i2c_addr=0x77)

    #setup sensor to begin reading data
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
    sensor.set_gas_heater_temperature(320)
    sensor.select_gas_heater_profile(0)
## da loop

    while(repeat > count) :
        if sensor.get_sensor_data():
            #now = datetime.now(%H/%M/%S)
            now = time.strftime("%d/%m/%Y")
            now2 = time.strftime("%H:%M:%S")
            temp = sensor.data.temperature
            # to fahrenheit
            temp = float(temp * (9/5) +32)
            pressure = sensor.data.pressure
            humidity = sensor.data.humidity
            gas = sensor.data.gas_resistance
            #print(now, temp, pressure, humidity, gas)
            print(now, now2, temp, pressure, humidity)
            #outList = [now, now2, temp, pressure, humidity]
            #myout = open("data.txt", "a")
            #myout.write(outList)
            count += 1
            time.sleep(wait_period)

if __name__ == '__main__':
    main()

        

