from kafka import KafkaConsumer
import os,time

if __name__ == "__main__":
	consumer = KafkaConsumer('Action')
	dict={'Start':10}
	for msg in consumer:
		id=msg.value.split(" ")[2]
		memSize=msg.value.split(" ")[3]
		if(id in dict):
			if(dict[id]!=memSize):
				os.system(msg.value)
				print(str(time.time())+"\t"+msg.value)
				dict.update({id:memSize})
		else:
			dict.update({id:memSize})
			os.system(msg.value)
			print(str(time.time())+"\t"+msg.value)