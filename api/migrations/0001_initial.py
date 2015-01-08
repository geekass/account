# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(auto_created=True, primary_key=True, serialize=False, editable=False, blank=True)),
                ('full_name', models.CharField(default=None, max_length=255)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('sign_up_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
