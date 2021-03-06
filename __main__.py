#!/usr/bin/env python
"""
Git-Puller

A RabbitMQ client and HTTP server.
"""

import os
import pika
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
HTTP_HOST = os.environ.get("HTTP_HOST") or "localhost"
HTTP_PORT = int(os.environ.get("HTTP_PORT") or 8000)
RABBIT_HOST = os.environ.get("RABBIT_HOST") or "localhost"
RABBIT_PORT = os.environ.get("RABBIT_PORT") or "5672"

app =  FastAPI()

def get_connexion():
    """Return the RabbitMQ connexion object."""
    return pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST+":"+RABBIT_PORT))

@app.get("/live")
def healthcheck():
    """Health check for Docker."""
    return "OK"

@app.get("/{repo}")
def webhook(repo: str):
    """Webhook to receive push notifications to send to the Rabbit."""
    print(f"Push : {repo}")
    with get_connexion() as connection:
        channel.basic_publish(
                exchange='',
                routing_key='push',
                body=repo
                )

if __name__ == "__main__":
    # Create the push queue
    with get_connexion() as connection:
        channel = connection.channel()
        channel.queue_declare(queue='push')
    uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
