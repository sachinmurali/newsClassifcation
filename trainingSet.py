import csv
import itertools
import urllib2
from bs4 import BeautifulSoup

# i = 3

try:
	with open('Reuter_data.csv', 'rb') as myFile:
		# reader = csv.reader(myFile)
		dialect = csv.Sniffer().sniff(myFile.read(), delimiters = ";,")
		myFile.seek(0)
		reader = csv.reader(myFile, dialect)
		# row_count = sum(1 for row in reader)
		# print row_count
		for row in itertools.islice(reader, 3, 4):
			link = row[0]

			page = urllib2.urlopen(link)

			soup = BeautifulSoup(page.read())

			for script in soup(["script", "style"]):
				script.extract()

			# get text
			text = soup.get_text()

			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())
			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)	 

			print text

			page.close()
except:
	pass			
