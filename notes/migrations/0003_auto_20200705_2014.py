# Generated by Django 3.0.5 on 2020-07-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200704_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='random',
            field=models.CharField(default='a123', max_length=200),
        ),
        migrations.AlterField(
            model_name='notes',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
