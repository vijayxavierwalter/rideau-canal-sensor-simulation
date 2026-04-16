# Rideau Canal Sensor Simulation

## Overview
This project simulates IoT sensors for the Rideau Canal monitoring system. It generates real-time telemetry data such as ice thickness and water temperature for multiple locations and sends the data to Azure IoT Hub.

The simulator mimics real-world environmental sensors and enables testing of the full Azure IoT pipeline.

### Technologies Used
- Python
- Azure IoT Device SDK (`azure-iot-device`)
- python-dotenv

---

## Prerequisites
- Python 3.10+
- Azure account
- Azure IoT Hub with a registered device
- Device connection string

---

## Installation

Clone the repository
git clone https://github.com/vijayxavierwalter/rideau-canal-sensor-simulation.git  
cd rideau-canal-sensor-simulation  
Created a .env file in the root directory:

## Usage   
python sensor_simulator.py

## Code Structure
rideau-canal-sensor-simulation/  
├── sensor_simulator.py   
├── requirements.txt  
├── .env.example  
├── config/  
│   └── sensor_config.json  

## Main Components
sensor_simulator.py
Connects to IoT Hub
Generates telemetry data
Sends messages

## Key Functions
get_telemetry()   
Generates random sensor data for:   
location   
ice thickness   
water temperature   
skating condition   
get_skating_condition()   
Determines skating quality based on ice thickness   
main()   
Initializes IoT client   
Sends telemetry in a loop  

## Key Functions

{
  "location": "string",  
  "iceThickness": "number",  
  "waterTemperature": "number",  
  "skatingCondition": "string",  
  "timestamp": "string"  
}


