# Generated by Django 2.2.1 on 2019-07-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='summary',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]