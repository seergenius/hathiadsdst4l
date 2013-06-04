'''This script is used to take a sample of 100,000 records from a Hathi Trust tab-delimited metadata file, 
or similar file, in order to make it easier to work with. The final function takes two arguments, the name of the file, and the delimiter.'''

import csv
import sys
csv.field_size_limit(sys.maxint)    #forces python to work with huge files

def open_tab_file(file_):
	csvfile=open(file_, 'r')
	R=csv.reader(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	return R

def open_comma_file(file_):
	csvfile=open(file_, 'r')
	R=csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	return R

def make_writer(name):
	csvfile=open(name+'.csv', 'wb+')
	W=csv.writer(csvfile, delimiter=',', quotechar='"')
	return W

def take_file_piece(file_, type):
	if type=='tab':
		R=open_tab_file(file_)
	elif type=='comma':
		R=open_comma_file(file_)
	else:
		print "Invalid file type. Valid file types are 'comma' and 'tab'"
	i=0
	W=make_writer(file_+'_smaller')
	for row in R:
		if i<100000:
			W.writerow(row)
			i+=1
		else:
			break
	return 0

take_file_piece('hathi_without_universityCodes.csv', 'comma')