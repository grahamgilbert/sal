# Generated by Django 1.10 on 2017-08-22 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0054_auto_20170705_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='os_family',
            field=models.CharField(choices=[(b'Darwin', b'macOS'), (b'Windows', b'Windows'), (
                b'Linux', b'Linux')], db_index=True, default=b'Darwin', max_length=256, verbose_name=b'OS Family'),
        ),
    ]
