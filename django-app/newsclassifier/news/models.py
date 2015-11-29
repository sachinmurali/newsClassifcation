from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    # article_num = models.CharField(max_length=100)
    article_title = models.TextField(max_length=100)
    article_content = models.TextField(max_length=1000)
    # article_url = models.URLField()
    article_category = models.TextField(max_length=100)
