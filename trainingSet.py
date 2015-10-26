import csv
import itertools
import urllib2
from bs4 import BeautifulSoup

i = 2

try:
	with open('BBC_data.csv', 'rb') as myFile:
		reader = csv.reader(myFile)
		# row_count = sum(1 for row in reader)
		# print row_count
		for row in itertools.islice(reader, 2, 3):
			link = row[0]
			page = urllib2.urlopen(link)
			print page.info()
			soup = BeautifulSoup(page.read())
			print soup.prettify()
			page.close()
except:
	pass			
