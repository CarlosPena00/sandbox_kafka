from kafka import KafkaProducer
from kafka.errors import KafkaError
from utils import BOOTSTRAP_SERVERS
from utils import json_to_bytes
from utils import TOPIC


producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=json_to_bytes,
    retries=3,
)

# Asynchronous by default
future = producer.send(TOPIC, dict(section="Asynchronous by default"))

# Block for 'synchronous' sends
try:
    metadata = future.get(timeout=10)
except KafkaError as e:
    # Decide what to do if produce request failed...
    print(e)

# Successful result returns assigned partition and offset
print(f"record_metadata: {metadata.topic=}, {metadata.partition=}, {metadata.offset=}")

# produce asynchronously
for idx in range(20):
    # The same key will always point to the same partition
    key = (f"{idx}").encode()
    producer.send(TOPIC, key=key, value=dict(section="json msg with key"))


def on_send_success(metadata):
    print(f"Callback: {metadata.topic=}, {metadata.partition=}, {metadata.offset=}")


def on_send_error(excp):
    # handle exception
    print("I am an errback", excp)


# produce asynchronously with callbacks
producer.send(TOPIC, dict(section="callback")).add_callback(
    on_send_success
).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()
