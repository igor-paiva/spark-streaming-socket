#! /usr/local/bin/python

# import os
import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

# os.environ["PYSPARK_PYTHON"] = sys.executable
# os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

conf = (
    SparkConf()
    .setMaster("spark://master:7077")
    .setAppName("StreamingWordCountSocketDistributed")
    .set("spark.driver.host", "submit")
    .set("spark.dynamicAllocation.enabled", "false")
    .set("spark.shuffle.service.enabled", "false")
    .set("spark.streaming.driver.writeAheadLog.closeFileAfterWrite", "true")
    .set("spark.streaming.receiver.writeAheadLog.closeFileAfterWrite", "true")
    .set("spark.executor.memory", "512m")
    .set("spark.executor.instances", "2")
    .set("spark.pyspark.python", "python3")
    .set("spark.pyspark.driver.python", "python3")
)

sc = SparkContext(conf=conf)

ssc = StreamingContext(sc, 1)


# ssc.checkpoint("hdfs://hadoop:9000/checkpoint")


lines = ssc.socketTextStream("socket", 9999)

words = lines.flatMap(lambda line: line.strip().split())

pairs = words.map(lambda word: (word, 1))

wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint(sys.maxsize)  # maxsize to print all elements

total_words = wordCounts.count()
total_words.pprint()

ssc.start()
ssc.awaitTermination()
