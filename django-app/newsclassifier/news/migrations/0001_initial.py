# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('article_title', models.TextField(max_length=100)),
                ('article_content', models.TextField(max_length=1000)),
                ('article_url', models.URLField()),
                ('article_category', models.TextField(max_length=100)),
            ],
        ),
    ]
