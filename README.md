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

## Run Kafka
```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```
