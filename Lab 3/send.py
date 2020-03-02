#!/usr/bin/env python
import pika

# Connect to localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Queue where message is sent
channel.queue_declare(queue='pingpong')

# Specify which queue the message is sent to
channel.basic_publish(exchange='',
                      routing_key='pingpong',
                      body='Ping!')
print(" [x] Sent 'Ping!'")

# Closing connection
connection.close()
