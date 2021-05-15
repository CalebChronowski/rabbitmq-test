import pika
import time
from datetime import datetime
from send import send

def main():
    parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2f')
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue='test-queue')
    print('opening connection\n...')
    while True:
        try:
            time.sleep(1)
            send(channel, str(datetime.now()))
            print('connection live')
        except KeyboardInterrupt:
            print('connection dead')
            break

    print('...\nclosing connection')
    connection.close()

if __name__ == "__main__":
    main()
