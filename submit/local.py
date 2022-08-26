import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "StreamingWordCountSocket")

ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("socket", 9999)

words = lines.flatMap(lambda line: line.strip().split())

pairs = words.map(lambda word: (word, 1))

wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint(sys.maxsize)  # maxsize to print all elements

total_words = wordCounts.count()
total_words.pprint()

ssc.start()
ssc.awaitTermination()
