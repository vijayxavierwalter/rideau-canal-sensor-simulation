import os
import time
import json
import random
from datetime import datetime, UTC
from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

LOCATIONS = ["Dow's Lake", "Fifth Avenue", "NAC"]


def get_skating_condition(ice_thickness: float) -> str:
    if ice_thickness >= 30:
        return "Excellent"
    elif ice_thickness >= 20:
        return "Good"
    elif ice_thickness >= 15:
        return "Fair"
    else:
        return "Poor"


def get_telemetry() -> dict:
    location = random.choice(LOCATIONS)
    ice_thickness = round(random.uniform(10.0, 35.0), 2)
    water_temperature = round(random.uniform(-5.0, 4.0), 2)

    return {
        "location": location,
        "iceThickness": ice_thickness,
        "waterTemperature": water_temperature,
        "skatingCondition": get_skating_condition(ice_thickness),
        "timestamp": datetime.now(UTC).isoformat()
    }


def main():
    if not CONNECTION_STRING:
        print("Error: IOTHUB_DEVICE_CONNECTION_STRING not found in .env file.")
        return

    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending Rideau Canal telemetry to IoT Hub...")

    try:
        while True:
            telemetry = get_telemetry()
            payload = json.dumps(telemetry)

            message = Message(payload)
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            client.send_message(message)
            print(f"Sent message: {payload}")
            time.sleep(10)

    except KeyboardInterrupt:
        print("Stopped sending messages.")

    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
