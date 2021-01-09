# Generated by Django 2.2.3 on 2019-07-14 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20190713_2131'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='count',
        ),
        migrations.RemoveField(
            model_name='users',
            name='food_id',
        ),
        migrations.CreateModel(
            name='Users_Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('food_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foods.Foods')),
                ('users_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
    ]
