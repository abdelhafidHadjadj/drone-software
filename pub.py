#! /usr/bin/env
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time, datetime
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, message):
    print("Message received: ", str(message.payload.decode("utf-8")))

mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_port = 1883 

client_id = "0001"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id)
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker, mqtt_port)

client.loop_start()

minLatitude = 36.7;  
maxLatitude = 36.8;  
minLongitude = 3.0; 
maxLongitude = 3.1; 

while True:
        position = {
        "vehicle_id" : client_id, 
        "lat" : str(uniform(minLatitude, maxLatitude)),
        "lng" : str(uniform(minLongitude, maxLongitude)),
        }
        client.publish(f"vehicle/position/{position['vehicle_id']}", json.dumps(position))
        print("Just published " + json.dumps(position) + " to Topic POSITION")
        time.sleep(1)