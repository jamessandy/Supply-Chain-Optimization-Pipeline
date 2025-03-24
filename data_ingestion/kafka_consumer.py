from kafka import KafkaConsumer
import json

def process_data(data):
    print(f"Processing: {data}")

consumer = KafkaConsumer(
    'supply_chain',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    process_data(message.value)