# My Kafka Sandbox

```sh
mamba env create
mamba activate kafka
pip-sync requirements-dev.txt
pre-commit install

# After update `setup.cfg`
pip-compile setup.cfg --resolver backtracking -o requirements.txt
pip-compile setup.cfg --resolver backtracking -o requirements-dev.txt --extra dev
```

## Install Kafka
```sh
# Regular Download (you should prefer docker)
wget https://downloads.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
tar zxvf kafka_*.tgz
cd kafka_*/

# Run the zookeeper and kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

```sh
# With docker (recommended)
docker compose up -d

# to execute .sh files, run:
docker exec -it kafka /bin/sh
```

## Learn
The kafka-*.sh are available inside kafka docker or in bin folder.

```sh
# Create topic
kafka-topics --create --zookeeper zookeeper-1:32181 --replication-factor 1 --partitions 1 --topic my_kafka_topic2

# List topics
kafka-topics --list --zookeeper zookeeper-1:32181

# Describe topics
kafka-topics --describe --bootstrap-server localhost:9092

# Topics in python
python src/simple/topic.py

# Producer in cmd (each line is a msg)
kafka-console-producer --broker-list localhost:9092 --topic my_kafka_topic
# Producer in Python
python src/simple/producer.py

# Consumer in cmd (from beginning)
kafka-console-consumer --bootstrap-server localhost:9092 --topic my_kafka_topic --from-beginning
# Consumer in Python
python src/simple/consumer.py
```
