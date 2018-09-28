# Generated by Django 1.10 on 2018-03-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0065_merge_20180219_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='os_family',
            field=models.CharField(choices=[(b'Darwin', b'macOS'), (b'Windows', b'Windows'), (b'Linux', b'Linux'), (b'ChromeOS', b'Chrome OS')], db_index=True, default=b'Darwin', max_length=256, verbose_name=b'OS Family'),
        ),
    ]
