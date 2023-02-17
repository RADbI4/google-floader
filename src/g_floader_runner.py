"""
Точка входа в приложение
"""
import pika
import time
import traceback
from main import upload_file

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='g_cloud_in')


def callback(ch, method, properties, body):
    try:
        print("Started")
        upload_file(body)
        print("Finished")
        time.sleep(60)
    except Exception as e:
        e = traceback.format_exc()
        # channel.basic_nack(delivery_tag=method)
        print(e)


channel.basic_consume(on_message_callback=callback, queue='g_cloud_in', auto_ack=True)
print(' [*] Waiting for messages, press CTRL+C to exit')
channel.start_consuming()