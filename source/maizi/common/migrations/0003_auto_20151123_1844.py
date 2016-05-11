# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_course_course_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careercourse',
            name='course_color',
            field=models.CharField(default=b'#50cd8e', max_length=50, verbose_name='\u8bfe\u7a0b\u914d\u8272'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_color',
            field=models.CharField(default=b'#429FDA', max_length=50, verbose_name='\u8bfe\u7a0b\u914d\u8272'),
        ),
    ]
