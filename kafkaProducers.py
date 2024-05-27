from kafka  import KafkaProducer
import json
import time
from data import get_register_user
# def get_partition(key,all,available):
#     print(key,all,available)
#     return 0
def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer)
#,partitioner=get_partition)

if __name__ == "__main__":
    while 1==1:
        registeruser = get_register_user()
        producer.send('test',registeruser)
        time.sleep(3)

