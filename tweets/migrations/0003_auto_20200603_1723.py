# Generated by Django 2.2 on 2020-06-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20200603_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweets',
            options={'ordering': ['-id']},
        ),
    ]