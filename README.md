# Nemo
This project is part of the ```Data Acquisition and Integration``` course of Kasetsart University.

## Overview
This project aims to investigate the variations in air quality at different altitudes within a multi-story building. Specifically, we are collecting data on

```
 - PM10 (Particulate Matter 10) (µg/m³)
 - PM2.5 (Particulate Matter 2.5) (µg/m³)
 - PM10 from third-party Web API (AQI)
 - PM2.5 from third-party Web API (AQI)
 - Smoke concentration (PPM)
 - Carbon monoxide (CO) (PPM)
 ```

 levels at ground level (7M), 4th floor (12M), and 18th floor(60M). The primary objective is to determine whether air quality is significantly affected by altitude within the building.

 The measured altitude is ***Height above mean sea level.***

 ## Project Components
1. **Hardware**

    Sensors Used:
    * PMS7003: Dust Sensor     *1 piece*
    * MQ-2: Smoke Gas Sensor   *1 piece*
    * MQ-9: CO Sensor          *1 piece*
    * KidBright Board          *1 board*

2. **API**

    We use ```Node-RED``` to collect PM10 and PM2.5 from 
    ```
    https://aqicn.org/city/
    ```
    to compare primary datas which come from our sensors and secondary datas which is come from Web API.

3. **Data Collection**

    The sensors continuously measure the concentration of PM10, PM2.5, smoke, and CO at the specified height and location. Data is collected at 1-Hour intervals and stored into *https://iot.cpe.ku.ac.th/pma* for later analysis. 
    
    Since we have only 1 sensor each, we have to measure each location one by one.

## Contributors

1. Wongsathorn Deekaoropkun 6310545353
2. Chinapat Rattanapirom 6310546317
3. Isaraa Phadungprasertkul b6410545801
