*** replace 172.19.152.4 with you wsl2 IP address

set-up java environment variable in vi /opt/hbase-1.4.13/conf/hbase-env.sh

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

start hbase
```bash
/opt/hbase-1.4.13/bin/start-hbase.sh
```

Ensure it is running http://172.19.152.4:44909/master-status

Run hbase shell and populate it with data
```bash
 hbase shell
```
```bash
 create 'test', 'cf'
 list 'test'
 put 'test', 'row1', 'cf:a', 'value1'
 put 'test', 'row2', 'cf:b', 'value2'
 put 'test', 'row3', 'cf:c', 'value3'
 describe 'test'
 get 'test', 'row1'
```
