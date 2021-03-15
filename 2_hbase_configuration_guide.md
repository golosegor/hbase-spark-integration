*** replace 172.19.152.4 with you wsl2 IP address

set-up java environment variable in vi /opt/hbase-1.4.13/conf/hbase-env.sh

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

configure bind addresses

```bash
<configuration>
    <property>
    <name>hbase.master.info.bindAddress</name>
    <value>172.19.152.4</value>
    <description>The address for the hbase master web UI
    </description>
  </property>
  <property>
    <name>hbase.regionserver.info.bindAddress</name>
    <value>172.19.152.4</value>
    <description>The address for the hbase regionserver web UI
    </description>
  </property>
</configuration>
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
 create 'Contacts', 'Personal', 'Office'
 list 'Contacts'
 put 'Contacts', '1000', 'Personal:Name', 'John Dole'
 put 'Contacts', '1000', 'Personal:Phone', '1-425-000-0001'
 put 'Contacts', '1000', 'Office:Phone', '1-425-000-0002'
 put 'Contacts', '1000', 'Office:Address', '1111 San Gabriel Dr.'
 put 'Contacts', '8396', 'Personal:Name', 'Calvin Raji'
 put 'Contacts', '8396', 'Personal:Phone', '230-555-0191'
 put 'Contacts', '8396', 'Office:Phone', '230-555-0191'
 put 'Contacts', '8396', 'Office:Address', '5415 San Gabriel Dr.'
 describe 'Contacts'
 scan 'Contacts'
```
