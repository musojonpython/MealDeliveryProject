# Generated by Django 2.2.3 on 2019-07-29 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20190719_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinks',
            name='count',
        ),
        migrations.RemoveField(
            model_name='foods',
            name='count',
        ),
        migrations.RemoveField(
            model_name='salads',
            name='count',
        ),
    ]
