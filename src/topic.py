import pprint
import time

from kafka.admin import KafkaAdminClient
from kafka.admin import NewTopic
from utils import BOOTSTRAP_SERVERS
from utils import TOPIC

admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS, client_id="test")

topic_list = []
topic_list.append(NewTopic(name=TOPIC, num_partitions=3, replication_factor=3))

topics = admin_client.list_topics()
print("Current Topics: ", topics)
if TOPIC in topics:
    admin_client.delete_topics(topics=[TOPIC])
    print(f"{TOPIC} was deleted")
time.sleep(0.5)

print("After delete:", print(admin_client.list_topics()))

admin_client.create_topics(new_topics=topic_list, validate_only=False)
print(f"A new {TOPIC} was created")
print("After Create:", admin_client.list_topics())

describe = admin_client.describe_topics(topics=[TOPIC])
pprint.pprint(describe, indent=2)
