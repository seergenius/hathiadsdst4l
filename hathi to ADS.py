import csv
import requests
import nltk
import json
from random import randint
sw=nltk.corpus.stopwords.words('english')
URL='http://adslabs.org/adsabs/api/search/'

#This function opens the csv of Astronomy and astrophysics related Hathi Trust records, produced by another script
def open_hathi_csv():
    csvfile=open('C:\\Users\\Jeremy\\Documents\\00Classes\\Spring 2013\\Data Scientist\\AstroHathiFile.csv', 'r')
    R=csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    outlist=[row for row in R]
    return outlist

#Takes a list of Hathi files and cleans out characters that will cause problems for the API
def title_cleaner(list_):
	for row in list_:
		row[11]=row[11].replace(';', '')
		row[11]=row[11].replace('\\', '')
		row[11]=row[11].replace('/', '')
		row[11]=row[11].replace('[', '')
		row[11]=row[11].replace(']', '')
		row[11]=row[11].replace(':', '')
	return 0

#splits the list into a dictionary by languages, with each language key corresponding to a list structured like the original list.
def list_splitter(list_):
	outdict={}
	for row in list_:
		lang=row[18]
		if lang not in outdict:
			outdict[lang]=[]
			outdict[lang].append(row)
		else:
			outdict[lang].append(row)
	return(outdict)

#strips out stopwords in a list of words
def rem_stops(lst):
    returnlist=[w for w in lst if w not in sw and len(w)>2]
    return returnlist

#Tokenizes a string and uses rem_stops to remove stopwords
def distill_title(title):
    rettitle=nltk.wordpunct_tokenize(title)
    rettitle=rem_stops(rettitle)
    return rettitle

#Takes a list of Hathi metadata and sends the cleaned title information to the ADS API as an unfielded search. Only searches one random ID at a time.
def ADS_single_request(list_, entry):
	title='+'.join(distill_title(list_[entry][11])[:7])
	print 'ADS Query: '+title
	year=list_[entry][16]
	Q={'dev_key':'8IIQgx5DrWZBwr2o', 'q':title, 'filter':year}
	ADSrequest=requests.get(URL, params=Q)
	ADSreturndict=ADSrequest.json()
	return ADSreturndict

'''def ADS_request(list_):
    for row in list_:
        title=row[11]
        year=row[16]
        Q={'dev_key':'8IIQgx5DrWZBwr2o', 'q':title, 'filter':year}
        ADSrequest=requests.get(URL, params=Q)
        ADSreturndict=ADSrequest.json()
    return 0'''

#uses previous functions to perform one random, english language query on the ADS.
#Will print the index, title and Hathi ID of the item searched for, then the unfielded search, then the number of hits in the ADS.
def one_rand_query():
	AstroHathiList=open_hathi_csv()
	title_cleaner(AstroHathiList)
	AstroHathiDict=list_splitter(AstroHathiList)
	engAstroHathiList=AstroHathiDict['eng']
	x=randint(1, len(engAstroHathiList))
	y=engAstroHathiList[x]
	print 'List Index: '+str(x)
	print 'HTID: '+y[0]
	print 'Title: '+y[11]
	print 'Year: '+y[16]
	reqDict=ADS_single_request(engAstroHathiList, x)
	if 'meta' in reqDict:
		print 'Hits in ADS: '+str(reqDict['meta']['hits'])
	else:
		print json.dumps(reqDict, sort_keys=True, indent=4, separators=(',', ': '))
	#print json.dumps(reqDict, sort_keys=True, indent=4, separators=(',', ': '))
	#Uncomment the line above to print the entire results json file.
	return 0

def one_nonrand_query(x):
	AstroHathiList=open_hathi_csv()
	title_cleaner(AstroHathiList)
	AstroHathiDict=list_splitter(AstroHathiList)
	engAstroHathiList=AstroHathiDict['eng']
	y=engAstroHathiList[x]
	print 'List Index: '+str(x)
	print 'HTID: '+y[0]
	print 'Title: '+y[11]
	print 'Year: '+y[16]
	reqDict=ADS_single_request(engAstroHathiList, x)
	if 'meta' in reqDict:
		print 'Hits in ADS: '+str(reqDict['meta']['hits'])
	else:
		print json.dumps(reqDict, sort_keys=True, indent=4, separators=(',', ': '))
	print json.dumps(reqDict, sort_keys=True, indent=4, separators=(',', ': '))
	#Uncomment the line above to print the entire results json file.
	return 0

one_rand_query()
#one_nonrand_query(430)