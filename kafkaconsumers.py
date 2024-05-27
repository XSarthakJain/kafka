# from kafka import KafkaConsumer\
#import kafka

from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        'test',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset = 'earliest',
        group_id = 'consumer_group1'
    )
    print("Consumer ============")
    for msg in consumer:
        print(f"Consumer Message ======={msg}")