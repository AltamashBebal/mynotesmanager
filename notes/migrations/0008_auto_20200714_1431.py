# Generated by Django 3.0.5 on 2020-07-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_notes_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=120, unique='False'),
        ),
    ]
