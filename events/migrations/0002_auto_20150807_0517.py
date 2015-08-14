# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='event',
            name='summary',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
