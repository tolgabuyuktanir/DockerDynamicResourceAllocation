from kafka import KafkaConsumer
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
prevUpdateCommand=""
def extractResourceUsage(out):
	allContainer=out.split(" ");
	allContainer = filter(None, allContainer)
	if(len(allContainer)==14 and (float(allContainer[12][:-1])>90 or float(allContainer[12][:-1])<10)):
		memoryOptimizer(allContainer[0],allContainer[5],float(allContainer[12][:-1]))
	return

def memoryOptimizer(id,totalMemory,memPerc):
	memoryUnit=totalMemory[-3:]
	tMem=totalMemory[:-3]
	factor=1
	global prevUpdateCommand
	if(memoryUnit=="GiB"):
		factor=factor*1024
	if(memPerc>90):
		factor=factor*2
	if(memPerc<10):
		factor=factor*0.5
	try:
		tMem=float(tMem)
		updateCommand="docker update "+id+" -m=\""+str(tMem*factor)+"mb"+"\""
		if(updateCommand!=prevUpdateCommand):
			print(str(time.time())+"\t"+updateCommand)
			producer.send('Action', b'%s' %updateCommand)
			prevUpdateCommand=updateCommand
	except ValueError:
		print("tMem tam sayi degil!")		
	return

if __name__ == "__main__":
	consumer = KafkaConsumer('Stats')
	for msg in consumer:
		extractResourceUsage(msg.value)