import csv
import sys
csv.field_size_limit(sys.maxint)    #forces python to work with huge files
BIG_FILE='hathi_full_20130601.txt'  #tab-separated hathi trust file. Retrieved from 'http://www.hathitrust.org/hathifiles'
SELECT_FILE='HathiIDs.csv'             #csv with gathered IDs. This is what I want to compare to the .tsv
OUT_NAME='Astro_Hathi.csv'
FIRST_ROW=['Volume Identifier', 'Access', 'Rights', 'University of Michigan record number', 'Enumeration/Chronology', 'Source', 'Source institution record number', 'OCLC numbers', 'ISBNs', 'ISSNs', 'LCCNs', 'Title', 'Imprint', 'Rights determination reason code', 'Date of last update', 'Government Document', 'Publication Date', 'Publication Place', 'Language', 'Bibliograhic Format']

def selectorListMaker(selectorFile):
    selectorCsv=open(selectorFile, 'rb')
    selectorReader=csv.reader(selectorCsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    selectorList=[]
    for row in selectorCsv:
        strRow = str(row).rstrip()
        selectorList.append(strRow)
    print 'Selector CSV opened.'
    return selectorList

def HathiReaderMaker(hathiFile):
    hathiCsv=open(hathiFile, 'r')
    hathiReader=csv.reader(hathiCsv, delimiter='\t', quotechar='"')
    print 'Hathi TSV opened.'
    return hathiReader

def outputWriterMaker(outputFile):
    outputCsv=open(outputFile, 'wb+')
    outputWriter=csv.writer(outputCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    print 'Output CSV opened.'
    return outputWriter

def compareIDs(selectorFile, hathiFile, outputFile):
    counter = 0
    matchcounter = 0
    selectorList = selectorListMaker(SELECT_FILE)
    hathiReader = HathiReaderMaker(BIG_FILE)
    outputWriter = outputWriterMaker(OUT_NAME)
    outputWriter.writerow(FIRST_ROW)
    for row in hathiReader:
        if counter%10000==0:
            print 'Processed '+str(counter)+' records. '+str(matchcounter)+' matches found.'
        counter+=1
        if row[0] in selectorList:
            outputWriter.writerow(row)
            matchcounter+=1
            del row
        else:
            del row
    return 0

compareIDs(SELECT_FILE, BIG_FILE, 'testOutput.csv')