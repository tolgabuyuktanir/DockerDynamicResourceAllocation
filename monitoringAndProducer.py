import time
from kafka import KafkaProducer
from subprocess import Popen, PIPE
import os



def run(command):
	process = Popen(command, stdout=PIPE, shell=True)
	while True:
		line = process.stdout.readline().rstrip()
		if not line:
			break
		yield line

producer = KafkaProducer(bootstrap_servers='localhost:9092')
#send one of every 10 reading
if __name__ == "__main__":
	for path in run("docker stats --format \"table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.MemPerc}}\t{{.PIDs}}\""):
		#if(int(time.time())%3==0):
		producer.send('Stats', b'%s' %path)
		print(path)
# if __name__ == "__main__":
#     for path in run("docker stats --format \"table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.MemPerc}}\t{{.PIDs}}\""):
#         producer.send('Stats', b'%s' %path)
#         print(path)