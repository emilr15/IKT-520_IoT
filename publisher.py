import paho.mqtt.client as mqtt
from time import sleep

#Sindre er en kukk


client_name = 'my_publisher'
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

def callback(client, userdata, message):
    print(message)


def run_publisher():
    client = mqtt.Client(client_name)
    client.on_connect = on_connect
    client.connect(host=broker_ip, port=broker_port)
    client.publish(topic, msg)
    client.message_callback_add(topic, callback)

    client.loop_forever()  # start the loop


run_publisher()
