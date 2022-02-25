#!/usr/bin/env python
"""Consummer of the queue."""

import sys, os
import pika

HOST = os.environ["HOST"]

def callback(ch, method, properties, body):
    """Called when a new event is received."""
    print(" [x] Received %r" % body)

def main():
    """Main function."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='push')
    channel.basic_consume(queue='push', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
