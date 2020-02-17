import paho.mqtt.client as mqtt
from time import sleep

client_name = 'my_publisher'
broker_ip = '127.0.0.1'
broker_port = 1883
qos_level = 2
topic = 'my_first_topic'
msg = 'ping'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'{client_name} is connected to broker on port: {broker_port}')
    else:
        print('Connection failed')

def on_publish(client, userdata, mid):
    print(f'message with ID: |{mid}| was delivered to broker.')

def run_publisher():
    # Initialising client
    client = mqtt.Client(client_name)

    # Declaring callback-functions for connecting and publishing
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connecting to broker
    client.connect(host=broker_ip, port=broker_port)

    # Publishing message to broker
    client.publish(topic, msg, qos=qos_level)

    # Starting loop
    client.loop_forever()  # start the loop


run_publisher()
