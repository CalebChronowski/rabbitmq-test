import pika

def send(channel, msg):
    channel.basic_publish(
        '',
        'test-queue1',
        msg,
        pika.BasicProperties(content_type='text/plain'))