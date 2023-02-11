import json

TOPIC = "my_topic"
BOOTSTRAP_SERVERS = ["localhost:9092", "localhost:9093", "localhost:9094"]


def json_to_bytes(j) -> bytes:
    return str.encode(json.dumps(j))


def bytes_to_json(b):
    return json.loads(b.decode())
