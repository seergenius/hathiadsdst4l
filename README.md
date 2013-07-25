hathiadsdst4l
=============
Project

This project began as an attempt to match articles possessed by the Hathi Trust with Articles in the Astrophysics Data System, in order to establish links between the two. The project only got as far as collecting a data set of articles under the subject heading for Astronomy and Astrophysics in the Hathi Trust Data set. However, this data set is useful in understanding the holdings of Hathi Trust which pertain to Astronomy and Astrophysics. The scripts used to generate this data set can also be adapted to systematically access metadata for other subject areas and queries within the Hathi Trust.

Data

The data collected consists of comma separated value spreadsheet with metadata from Hathi Trust’s tab delimited Hathifiles. Field descriptions are available at the previous link. The data consists mostly of documents available in the public domain, but some articles not available in the public domain are included because of the way that the data was accessed.
AstroHathi.csv

Scripts

There are several scripts, each with its own purpose, all written in Python, using an Enthought Python 2.7 distribution. One script uses regular expressions to collect IDs from Hathi Trust search results pages, then uses those IDs, which represent aggregate records sometimes consisting of multiple scanned documents, to collect the individual Hathi Trust Identifiers for each item in the search results. These identifiers are compared in another script to a monthly Hathi File, which then outputs the final data set.
GetHathiIDs.py
reduceHathiFile.py

All other files are test files.
