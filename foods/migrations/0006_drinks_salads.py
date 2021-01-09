# Generated by Django 2.2.3 on 2019-07-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_foods_check_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('images', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('check_field', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('images', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('check_field', models.BooleanField(default=True)),
            ],
        ),
    ]
