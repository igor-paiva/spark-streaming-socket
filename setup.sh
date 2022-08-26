echo "Downloading Spark 3.1.3"
echo ""

wget https://dlcdn.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-hadoop3.2.tgz

tar xzf spark-3.1.3-bin-hadoop3.2.tgz

rm spark-3.1.3-bin-hadoop3.2.tgz

echo "Creating docker network"
echo ""

docker network create spark-socket-cluster || true

echo "Initializing containers"
echo ""

docker-compose up
