# Generated by Django 3.0.5 on 2020-07-08 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20200705_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='fileName',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
