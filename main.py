# Johnny Wong
# SSW599 Smart City Lab

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# visualize the data: 
# Does the data from out1dat indicate the approaching storm? If so, how?
# Time     Temperature  Pressure  Humidity 
# 11-09-2022 to 11-10-2022
def readData():
    df = pd.read_csv('./out1dat', sep=' ')
    df = df.iloc[:,[1,2,3,4]]
    headers = ['Time', 'Temperature', 'Pressure', 'Humidity']
    df.columns = headers
    return df

def visualizeTemperature(df):
    temperature = df.iloc[:, [0, 1]]
    line = temperature.plot.line(color='orange')
    return line
    
def visualizePressure(df):
    pressure = df.iloc[:, [0, 2]]
    line = pressure.plot.line(color='blue')
    return line 
    
def visualizeHumidity(df):
    humidity = df.iloc[:, [0, 3]]
    print(humidity)
    line = humidity.plot.line(color='purple')
    return line 
    
def main():
    df = readData()
    visualizeTemperature(df)
    visualizePressure(df)
    visualizeHumidity(df)
    plt.show()
    return 1

if __name__ == '__main__':
    main()