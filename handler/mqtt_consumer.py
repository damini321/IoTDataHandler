import sys
import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(userdata)

def on_message(client, userdata, msg):
    print("Received message from MQTT:")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode())  # Decode payload bytes to string
    # Insert data into MongoDB collection
    try:
        collection.insert_one({"topic": msg.topic, "payload": msg.payload.decode()})
        print("Data inserted into MongoDB")
    except Exception as e:
        print(f"Error inserting data into MongoDB: {e}")

def mqtt_consumer():
    if len(sys.argv) != 2:
        print("Usage: python mqtt_consumer.py <topic>")
        return
    
    topic = sys.argv[1]

    client = mqtt.Client(userdata=topic)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)

    print("MQTT message consumer started. Waiting for messages...")
    client.loop_forever()

if __name__ == "__main__":
    mqtt_consumer()

