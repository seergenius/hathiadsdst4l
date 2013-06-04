import csv

def open_abbr_data(file_):
	csvfile=open(file_+'.csv', 'r')
	R=csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	abbrList=[row for row in R]
	return abbrList

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

def rewrite_list(abbrfile, valfile, index):
	abbrList = open_abbr_data(abbrfile)
	valDict = dictify_values(valfile)
	for row in abbrList:
		row[index]=valDict[row[index]]
	return abbrList

def write_better_file(abbrfile, valfile, index):
	fileList=rewrite_list(abbrfile, valfile, index)
	csvfile=open(abbrfile+'_no_abbr.csv', 'wb+')
	W=csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in fileList:
		W.writerow(row)
	return 0

def error_report(abbrfile, valfile, index):
	abbrList = open_abbr_data(abbrfile)
	valDict = dictify_values(valfile)
	errorlist=[]
	for row in abbrList:
		if row[index] not in valDict:
			errorlist.append([row[0], row[index]])
	csvfile=open(valfile+'_error_report.csv', 'wb+')
	W=csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in errorlist:
		W.writerow(row)
	return errorlist

#Each abbreviation list one at a time:
#write_better_file('AstroHathiFile', 'MARC_languages', 18)
#write_better_file('AstroHathiFile', 'universityCodes', 5)
#write_better_file('AstroHathiFile', 'attributes', 2)
#write_better_file('AstroHathiFile', 'rightsDetermination', 13)
#write_better_file('AstroHathiFile', 'materialType', 19)
#write_better_file('AstroHathiFile', 'MARCcountries', 17)

#all at once:
rewrite_list('AstroHathiFile', 'MARC_languages', 18)
rewrite_list('AstroHathiFile', 'universityCodes', 5)
rewrite_list('AstroHathiFile', 'attributes', 2)
rewrite_list('AstroHathiFile', 'rightsDetermination', 13)
rewrite_list('AstroHathiFile', 'materialType', 19)
write_better_file('AstroHathiFile', 'MARCcountries', 17)