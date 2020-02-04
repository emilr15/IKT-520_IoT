import paho.mqtt.client as mqtt
from time import sleep

client_name = 'my_publisher'
broker_ip = '127.0.0.1'
broker_port = 1883
topic = 'my_first_topic'
msg = 'ping'
msg2 = 'pingelipong'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'{client_name} is connected to broker on port: {broker_port}')
        client.subscribe(topic, qos=0)
    else:
        print('Connection failed')

def on_publish(client, userdata, mid):
    print(f'message with ID: |{mid}| was delivered to broker.')


def on_subscribe(client):
    pass

def run_publisher():
    client = mqtt.Client(client_name)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(host=broker_ip, port=broker_port)
    client.publish(topic, msg, qos=0)
    for i in range(5):
        sleep(0.5)
        client.publish(topic, msg2, qos=1)

    client.loop_forever()  # start the loop


run_publisher()
