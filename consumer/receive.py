import pika

parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2f')
channel = None
flow = None

# Step #2
def on_connected(connection):
    """Called when we are fully connected to RabbitMQ"""
    # Open a channel
    connection.channel(on_open_callback=on_channel_open)

# Step #3
def on_channel_open(new_channel):
    """Called when our channel has opened"""
    global channel
    channel = new_channel
    channel.queue_declare(queue="test-queue1", durable=True, exclusive=False, auto_delete=False, callback=on_queue_declared) # These parameters need to be carefully chosen. They were not carefully chosen.

# Step #4
def on_queue_declared(frame):
    """Called when RabbitMQ has told us our Queue has been declared, frame is the response from RabbitMQ"""
    channel.basic_consume('test-queue1', handle_delivery, callback=msg)

# Step #5
def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    msg(body)
    # return body
    # if body == b'0' or body == b'1':
    #     print('arrived here')
    #     if flow != bool(int(body)):
    #         flow = bool(int(body))
    # else:
    #     if flow:
    #         print(f'flow 1: {flow}')
    #         # print(body)
    #     else:
    #         print(f'flow 0: {flow}')
    #         # print(body)

def msg(msg):
    if msg == b'1':
        yield 'Holyshit!'
    else:
        yield msg
# Step #1: Connect to RabbitMQ using the default parameters
parameters = pika.ConnectionParameters()
connection = pika.SelectConnection(parameters, on_open_callback=on_connected)

def run():
    try:
        # Loop so we can communicate with RabbitMQ
        connection.ioloop.start()
    except KeyboardInterrupt:
        # Gracefully close the connection
        connection.close()
        # Loop until we're fully closed, will stop on its own
        connection.ioloop.start()

if __name__ == "__main__":
    run()