import feedparser
import urllib2
from bs4 import BeautifulSoup

class NewsAggregator(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.training_data = []
		self.articles = []

	def feedreader(self):
		# rss_feeds = ['http://news.yahoo.com/rss/','http://feeds.bbci.co.uk/news/rss.xml#','http://news.google.com/news?cf=all&hl=en&pz=1&ned=us&output=rss', 'http://www.wsj.com/xml/rss/3_7085.xml'
			# 'http://www.wsj.com/xml/rss/3_7201.xml', 'http://www.wsj.com/xml/rss/3_7455.xml', 'http://feeds.feedburner.com/TechCrunch/', 'http://feeds.coloradodaily.com/mngi/rss/CustomRssServlet/25/219104.xml']
		rss_feeds = ['http://feeds.bbci.co.uk/news/rss.xml#']
		for link in rss_feeds:
			feed = feedparser.parse(link)
			for item in feed.entries:
				link = item['links'][0]['href']
				title = item['title']
				time_published = item['published']

				self.articles.append({'link' : link, 'title' : title, 'time' : time_published})
		# print len(self.articles)
		return self.getArticles()

	def getArticles(self):
		for article in self.articles:
			try:
				# print row
				link = article['link']

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
				self.training_data.append(({'content': text, 'title': article['title']}))

				page.close()

			except Exception, e:
				print e
				continue
		return self.training_data

if __name__ == "__main__":
	na = NewsAggregator()
	na.feedreader()
	na.getArticles()
