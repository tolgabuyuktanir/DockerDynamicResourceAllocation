# DockerDynamicResourceAllocation

**randomNumberSort.py**

python randomNumberSort.py param1 param2 

	-param1 : repetation
	
	-param2 : number of random values
	
**createMultipleContainer.sh**

```./createMultipleContainer.sh```

This is bash script which creates ten times a container and runs randomNumberSort.py.

**monitoringAndProducer.py**

```python monitoringAndProducer.py```

Reads all containers stats and send to Apache Kafka.

**statsConsumerActionProducer.py**

```python statsConsumerActionProducer.py```

Gets status of  running container from Apache Kafka. If the container is using memory more than %90, creates command to double up memory resource and sends to Action Topic of Apache Kafka. On the other hand, the container is using memory less than %10, the message is created to take back half of the allocated memory resource in this script. It's repeated for each container.

**actionComsumerResourceUpdate.py**

```python actionComsumerResourceUpdate.py```

Reads update commands from Apache Kafka and execute them on Docker Daemons.




If you get warning showed below: 

  WARNING: Your kernel does not support cgroup swap limit.
	
**Solution:**
```bash
  1- Edit the /etc/default/grub file. Add or edit the GRUB_CMDLINE_LINUX line as GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
	
  2- update grub with sudo update-grub
	
  3- Reboot	

```
