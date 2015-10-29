import csv
import itertools
import urllib2
from bs4 import BeautifulSoup

try:
	train_data = []
	with open('Reuter_data.csv', 'rb') as myFile:
		# reader = csv.reader(myFile)
		# dialect = csv.Sniffer().sniff(myFile.read(), [',',';'])
		# myFile.seek(0)
		# reader = csv.reader(myFile, dialect)
		# row_count = sum(1 for row in reader)
		# print row_count
		# print row_count
		reader = csv.reader(myFile, delimiter=';', quotechar='|')

		for row in reader:
			# print row
			link = row[0]

			page = urllib2.urlopen(link)

			soup = BeautifulSoup(page.read())

			for script in soup(["header", "nav", "footer", "script", "style"]):
				script.extract()
			for div in soup.findAll('div', 'column2 grid4'):
				div.extract()

			# get text
			text = soup.get_text()

			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())
			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)

			# add to dict
			train_data.append({
				'url': link,
				'content': text,
				'class': row[1]
			})
			ipdb.set_trace()  ######### Break Point ###########

			page.close()
	print train_data
except:
	pass
