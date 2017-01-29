#!/usr/local/bin/python

import serial
import time
import datetime

data = []

i = 0

ser = serial.Serial('/dev/cu.usbmodem621',9600)

while True:
	received_line=ser.readline().rstrip()
	timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	entry = [timestamp]
	entry.append(received_line.split(':')[0])
	entry.append(received_line.split(':')[1])
	data.append(entry)
	# print myList
	print data[i]

	with open("data_log.csv","a+") as myfile:
		number_of_columns_in_entry = len(data[i])
		for x in range (0,number_of_columns_in_entry):
    			myfile.write(str(data[i][x]))
    			if x < number_of_columns_in_entry-1:
    					myfile.write(",")
	with open("data_log.csv","a+") as myfile:
    		myfile.write("\n")
	i += 1