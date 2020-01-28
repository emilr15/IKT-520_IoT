import paho.mqtt.client as mqtt
from time import sleep


client_name = 'my_subscriber'
broker_ip = '127.0.0.1'
broker_port = 1883
topic = 'my_first_topic'
msg = 'ping'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'{client_name} is connected to broker')
        client.subscribe(topic, qos=1)
    else:
        print('Connection failed')

def on_message(client, userdata, message):
    if message.payload.decode() == msg:
        print('pong')

def run_subscriber():
    client = mqtt.Client(client_name)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=broker_ip, port=broker_port)

    client.loop_forever()


run_subscriber()