from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.
def main(request):
    t = get_template("landingpage.html")
    html = t.render(Context({}))
    return HttpResponse(html)

def index(request):
    t = get_template("index.html")
    html = t.render(Context({}))
    return HttpResponse(html)
