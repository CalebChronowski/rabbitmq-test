import pika
import time
from random import randrange
from datetime import datetime
from send import send

def main():
    parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2f')
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue='test-queue')
    print('opening connection 2\n...')
    while True:       # this loop sends either a 1 or a 0 at random intervals between 1s to 10s
        try:
            n = randrange(1,11)
            msg = n
            print(f'next message in {n}s')
            while n>0:
                n -= 1
                time.sleep(1)
                print('connection 2 live')
            send(channel, str(msg % 2))
        except KeyboardInterrupt:
            print('connection 2 dead')
            break

    print('...\nclosing connection 2')
    connection.close()

if __name__ == "__main__":
    main()
