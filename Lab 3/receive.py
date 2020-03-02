#!/usr/bin/env python
import pika

# Connect to localhost
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Select queue
channel.queue_declare(queue='pingpong')

# Prints pong if recieved message is Ping!, else: error.
def callback(ch, method, properties, body):
    if body.decode() == 'Ping!':
        print('Pong')
    else:
        print('Message not received')

# Recieve messages from pinpong queue
channel.basic_consume(queue='pingpong', on_message_callback=callback, auto_ack=True)

# If reciever gets the ping message, send.py prints Pong!.



print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
