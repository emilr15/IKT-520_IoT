import paho.mqtt.client as mqtt
from time import sleep


client_name = 'my_subscriber'
broker_ip = '127.0.0.1'
broker_port = 1883
topic = 'my_first_topic'
msg = 'ping'
qos_level = 2


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'{client_name} is connected to broker on port: {broker_port}')
        client.subscribe(topic, qos=0)
    else:
        print('Connection failed')

def on_message(client, userdata, message):
    # Checking if message payload is 'ping', if yes 'pong' is printed
    if message.payload.decode() == msg:
        print('pong')

def run_subscriber():
    # Initialising client
    client = mqtt.Client(client_name)

    # Declaring callback-functions for connecting and receiving messages
    client.on_connect = on_connect
    client.on_message = on_message

    # Connecting to broker
    client.connect(host=broker_ip, port=broker_port)

    client.loop_forever()


run_subscriber()