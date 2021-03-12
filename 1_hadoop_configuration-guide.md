*** replace 172.19.152.4 with you wsl2 IP address

set-up host name binding for hdfs in /opt/hadoop-2.8.5/etc/hadoop/hdfs-site.xml

```xml

<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

set-up default fs in /opt/hadoop-2.8.5/etc/hadoop/core-site.xml

```xml

<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://172.19.152.4:9000</value>
    </property>
</configuration>
```

set-up in /opt/hadoop-2.8.5/etc/hadoop/mapred-site.xml 
```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=/opt/hadoop-2.8.5</value>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=/opt/hadoop-2.8.5</value>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=/opt/hadoop-2.8.5</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>
            $HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*,$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*,$HADOOP_MAPRED_HOME/share/hadoop/common/*,$HADOOP_MAPRED_HOME/share/hadoop/common/lib/*,$HADOOP_MAPRED_HOME/share/hadoop/yarn/*,$HADOOP_MAPRED_HOME/share/hadoop/yarn/lib/*,$HADOOP_MAPRED_HOME/share/hadoop/hdfs/*,$HADOOP_MAPRED_HOME/share/hadoop/hdfs/lib/*
        </value>
    </property>
</configuration>
```

set-up java home directory in /opt/hadoop-2.8.5/etc/hadoop/hadoop-env.sh
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

format data
```bash
hdfs namenode -format
```

start everything
```bash
/opt/hadoop-2.8.5/sbin/start-all.sh
```


ensure data could be saved / received
```bash
hadoop fs -ls hdfs://172.19.152.4:9000/
hadoop fs -mkdir hdfs://172.19.152.4:9000/my-test-folder
hadoop fs -ls hdfs://172.19.152.4:9000/
```