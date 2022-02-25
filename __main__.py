#!/usr/bin/env python
"""
Git-Puller

A RabbitMQ client and HTTP server.
"""

import os
import pika
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
HTTP_HOST = os.environ["HTTP_HOST"] or "localhost"
HTTP_PORT = int(os.environ["HTTP_PORT"] or 8000)
RABBIT_HOST = os.environ["RABBIT_HOST"] or "localhost"
RABBIT_PORT = os.environ["RABBIT_PORT"] or "5672"

app =  FastAPI()

def get_connexion():
    return pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST+":"+RABBIT_PORT))


@app.route("/push/{repo}", methods=["GET"])
def webhook():
    repo = requests
    with get_connexion() as connection:
        channel.basic_publish(
                exchange='',
                routing_key='push',
                body='repod!'
                )
# print(" [x] Sent 'Hello World!'")

if __name__ == "__main__":
    # Create the push queue
    with get_connexion() as connection:
        channel = connection.channel()
        channel.queue_declare(queue='push')
    app.run(host=HTTP_HOST, port=HTTP_PORT)
