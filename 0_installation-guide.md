download
 - HBase: 1.4.13: https://ftp.cixug.es/apache/hbase/1.4.13/hbase-1.4.13-bin.tar.gz
 - Hadoop: 2.8.5 https://archive.apache.org/dist/hadoop/common/hadoop-2.8.5/hadoop-2.8.5.tar.gz
 - Spark: 2.4.5 https://ftp.cixug.es/apache/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz

Unzip in wsl to local folder:
tar xvzf hbase-1.4.13-bin.tar.gz -C /opt

sudo tar -xf hbase-1.4.13-bin.tar.gz -C /opt/
sudo tar -xf hadoop-2.8.5.tar.gz -C /opt/
sudo tar -xf spark-2.4.7-bin-hadoop2.7.tgz -C /opt/

sudo chmod 777 -R /opt/hadoop-2.8.5
sudo chmod 777 -R /opt/hbase-1.4.13
sudo chmod 777 -R /opt/spark-2.4.7-bin-hadoop2.7
