import json

TOPIC = "my_kafka_topic"
BOOTSTRAP_SERVERS = ["localhost:9092"]


def json_to_bytes(j) -> bytes:
    return str.encode(json.dumps(j))


def bytes_to_json(b):
    return json.loads(b.decode())
