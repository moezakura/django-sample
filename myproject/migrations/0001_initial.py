# Generated by Django 2.2.3 on 2019-07-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=65535)),
                ('post_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
