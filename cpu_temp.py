import matplotlib.pyplot as plt
from gpiozero import CPUTemperature
from time import sleep, strftime, time

# Create a cpu object
cpu = CPUTemperature()
print(cpu.temperature)

#Turn on interactive mode
plt.ion()

#Initialize lists for plotting
x = []
y = []

#Define a path to the CSV file within the 'temperature_logger' folder
csv_file_path = "/home/liand/temperature_logger/cpu_temp.csv"

#Get the current date and time as a string
timestamp = strftime("%Y-%m-%d %H:%M:%S")

def write_temp(temp):
	with open(csv_file_path, "a") as log:
		log.write("{0},{1}\n".format(timestamp,str(temp)))

def graph(temp):
	y.append(temp)
	x.append(time())
	plt.clf()
	plt.scatter(x,y)
	plt.plot(x,y)
	plt.draw()
	
while True:
	temp = cpu.temperature
	write_temp(temp)
	graph(temp)
	plt.pause(1)
