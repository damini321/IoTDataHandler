# IoTDataHandler


## MQTT Message Handler

### Overview
This repository contains Python scripts to handle MQTT messages using RabbitMQ as the message broker and MongoDB for data storage. The provided scripts allow publishing messages to specific topics and consuming messages from subscribed topics.

### Prerequisites
- Python 3
- Paho MQTT library (`pip install paho-mqtt`)
- RabbitMQ installed and configured with MQTT plugin enabled
- MongoDB installed and running on localhost

### Installation Instructions

#### RabbitMQ
1. **Download RabbitMQ**: Visit the [RabbitMQ download page](https://www.rabbitmq.com/download.html) and download the appropriate installer for your operating system.
2. **Install RabbitMQ**: Follow the installation instructions provided for your operating system on the RabbitMQ website.
3. **Enable MQTT Plugin**: Once RabbitMQ is installed, enable the MQTT plugin by running the following command:
   ```bash
   rabbitmq-plugins enable rabbitmq_mqtt

#### Start RabbitMQ Server: Start the RabbitMQ server using the provided command or service manager.
### MongoDB
1. **Download MongoDB**: Visit the MongoDB download page and download the appropriate installer for your operating system.
2. **Install MongoDB**: Follow the installation instructions provided for your operating system on the MongoDB website.
3. **Start MongoDB Server**: Start the MongoDB server by running the following command:
'mongod'
- This command will start the MongoDB server on the default port (27017) and use the default data directory.
4. Verify MongoDB Installation: Open a new terminal window and run the MongoDB shell by typing mongo. If MongoDB is installed correctly, you should see the MongoDB shell prompt.

#### Usage
'mqtt_publisher.py'
- Publishes a message to a specific MQTT topic.

### Usage:
'python mqtt_publisher.py <topic> <message>'

- Example:
'python mqtt_publisher.py test1 "test message 1"

### mqtt_consumer.py
Subscribes to an MQTT topic and inserts received messages into MongoDB.

### Usage:
'python mqtt_consumer.py <topic>'

- Example:
'python mqtt_consumer.py test1'

## Configuration
Ensure RabbitMQ is installed and the MQTT plugin is enabled. MongoDB should be running on localhost.

## Conclusion
This project offers a robust solution for MQTT message handling, integrating RabbitMQ for message queuing and MongoDB for data storage. With easy setup and usage, it provides scalability and reliability for managing IoT data. Contributions are welcome to further enhance its capabilities and address any issues.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
