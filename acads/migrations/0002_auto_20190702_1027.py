# Generated by Django 2.2.1 on 2019-07-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acadsmodel',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]