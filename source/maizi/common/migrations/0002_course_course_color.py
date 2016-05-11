# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_color',
            field=models.CharField(default='#429FDA', max_length=50, verbose_name='\u8bfe\u7a0b\u914d\u8272'),
            preserve_default=False,
        ),
    ]
