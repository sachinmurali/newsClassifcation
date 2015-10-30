import csv
import itertools
import urllib2
from bs4 import BeautifulSoup
import cPickle as pickle
import sys

class DataExtractor(object):
	def __init__(self):
		self.training_data = []

	def SetCSVFileName(self, filename):
		self.csvFilename = filename

	def GetTrainingData(self):
		return self.training_data;

	def ReadPickledData(self):
		with open('data_dump', 'rb') as dump_file:
			pickled_data = pickle.load(dump_file);
			return pickled_data

	def GetArticles(self):
		with open(self.csvFilename, 'rb') as myFile:
			reader = csv.reader(myFile, delimiter=';', quotechar='|')

			for row in reader:
				try:
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
					self.training_data.append({
						'url': link,
						'content': text,
						'class': row[1]
					})

					page.close()
				except Exception, e:
					print e
					continue
		# print train_data
		with open('data_dump', 'wb') as dump:
			pickle.dump(self.training_data, dump, pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
	# simple test to test all the functions in the class
	# a = DataExtractor()
	# a.SetCSVFileName('Reuter_data.csv')
	# a.GetArticles()
	# print a.ReadPickledData()
