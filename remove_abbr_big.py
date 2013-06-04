import csv
import sys
csv.field_size_limit(sys.maxint)    #forces python to work with huge files

def open_value_csv(file_):
	csvfile=open(file_+'.csv', 'r')
	R=csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	valueList=[row for row in R]
	#data massaging. comment out lines that are unneeded, or iteration if none is needed.
	if file_== 'MARC_languages' or 'MARCcountries':
		for row in valueList:
			if '-' in row[0]:
				row[0]=row[0].replace('-', '') #Used for MARC language codes
				row[1]=row[1]+' (Discontinued code)'
	if file_ == 'MARCcountries':
		for row in valueList:
			if len(row[0])==2:
				row[0]=row[0]+' '
	return valueList

def dictify_values(file_):
	returndict={}
	valList=open_value_csv(file_)
	for row in valList:
		returndict[row[0]]=row[1]
	return returndict

def open_abbr_data(file_):
	csvfile=open(file_, 'r')
	R=csv.reader(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	return R

def remove_abbr(abbrfile, valfile, index):
	abbrCSV = open_abbr_data(abbrfile)
	valDict = dictify_values(valfile)
	csvfile=open(abbrfile+'_without_'+valfile+'.csv', 'wb+')
	W=csv.writer(csvfile, delimiter=',', quotechar='"')
	for row in abbrCSV:
		row[index]=valDict[row[index]]
		W.writerow(row)
		del row
	return 0

#remove_abbr('hathi_full_20130501.txt', 'MARC_languages', 18)
#remove_abbr('hathi_full_20130501.txt', 'MARCcountries', 17)
remove_abbr('hathi_full_20130501.txt', 'universityCodes', 5)