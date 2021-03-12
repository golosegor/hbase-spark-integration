"""
A simple example demonstrating Spark HBase data sources.
Run with:
  spark-submit --packages com.hortonworks:shc:1.0.0-1.6-s_2.10 --repositories http://repo.hortonworks.com/content/groups/public/ --files /opt/cloudera/parcels/CDH/lib/hbase/conf/hbase-site.xml example.py
"""
import pyspark
from pyspark.sql import SparkSession


def hbase_read_demo(spark: SparkSession):
    # ''.join(string.split()) in order to write a multi-line JSON string here.
    catalog = ''.join("""{
        "table":{"namespace":"default", "name":"Contacts"},
        "rowkey":"key",
        "columns":{
            "rowkey":{"cf":"rowkey", "col":"key", "type":"string"},
            "officeAddress":{"cf":"Office", "col":"Address", "type":"string"},
            "officePhone":{"cf":"Office", "col":"Phone", "type":"string"},
            "personalName":{"cf":"Personal", "col":"Name", "type":"string"},
            "personalPhone":{"cf":"Personal", "col":"Phone", "type":"string"}
        }
    }""".split())

    # Writing
    # df.write \
    #    .options(catalog=catalog) \
    #    .format(data_source_format) \
    #    .save()

    # Reading
    data_source_format = 'org.apache.spark.sql.execution.datasources.hbase'
    df = spark.read \
        .options(catalog=catalog) \
        .format(data_source_format) \
        .load()

    df.show(2)


def create_spark_session() -> SparkSession:
    number_cores = 8
    memory_gb = 8
    conf = (
        pyspark.SparkConf()
            .setMaster(f'local[{number_cores}]')
            .set('spark.driver.memory', f'{memory_gb}g')
            .set('spark.sql.streaming.forceDeleteTempCheckpointLocation', 'true')
    )
    sc = pyspark.SparkContext(conf=conf).getOrCreate()
    sc.setLogLevel("WARN")
    session = pyspark.sql.SparkSession(sc)
    return session


if __name__ == "__main__":
    spark_session = create_spark_session()
    hbase_read_demo(spark_session)
    spark_session.stop()
