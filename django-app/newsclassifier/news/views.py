from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from classifier import Classifier
from feedReader import NewsAggregator
import numpy as np
import cPickle as pickle
from news.models import Article
import json
from django.core import serializers

# Create your views here.
def main(request):
    t = get_template("landingpage.html")
    html = t.render(Context({}))
    return HttpResponse(html)

def index(request):
    t = get_template("index.html")
    html = t.render(Context({}))
    return HttpResponse(html)

def RetrieveArticles(request):
    cat = request.GET['category']
    # print cat
    all_entries = Article.objects.all().filter(article_category=cat)
    entries = []
    for element in all_entries:
        entries.append(serializers.serialize('json', [element,]))
    # print entries
    return HttpResponse(json.dumps(entries))

def GetNewArticles(request):
    # Get the articles from RSS
    # aggregator = NewsAggregator()
    # list_of_articles = aggregator.feedreader()
    classifier = Classifier("filename.pkl")
    # Predict
    list_of_classes = []
    # with open("articles_dump", "wb") as dump:
    #     pickle.dump(list_of_articles, dump, pickle.HIGHEST_PROTOCOL)
    with open("articles_dump") as dump:
        list_of_articles = pickle.load(dump)
    for article in list_of_articles:
        list_of_classes.append(article["content"])
    # print list_of_classes
    res = classifier.predict(np.asarray(list_of_classes))

    for i in range(0, len(list_of_articles)):
        if res[i] == 1:
            cat = "Sports"
        elif res[i] == 2:
            cat = "Economy_business_finance"
        elif res[i] == 3:
            cat = "Science_technology"
        else:
            cat = "Lifestyle_leisure"
        element = list_of_articles[i]
        list_of_articles[i]["category"] = cat
        article = Article(article_title=element["title"], article_content=element["content"], article_category=cat)
        article.save()
    json_object = json.dumps(list_of_articles)
    return HttpResponse(json_object)
