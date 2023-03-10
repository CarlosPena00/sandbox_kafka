from kafka import KafkaConsumer
from utils import BOOTSTRAP_SERVERS
from utils import bytes_to_json
from utils import TOPIC

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    TOPIC,
    group_id="consumer",
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=bytes_to_json,
    consumer_timeout_ms=500,
    max_poll_records=1,
)
while True:
    print("*" * 88)
    for message in consumer:
        print(
            f"{message.topic}:{message.partition}:{message.offset}: "
            f"key={message.key} value={message.value}"
        )
