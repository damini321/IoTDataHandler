import sys
import paho.mqtt.publish as publish

def main():
    if len(sys.argv) != 3:
        print("Usage: python mqtt_publisher.py <topic> <message>")
        return
    
    topic = sys.argv[1]
    message = sys.argv[2]

    publish.single(topic, message, hostname="localhost")

if __name__ == "__main__":
    main()

