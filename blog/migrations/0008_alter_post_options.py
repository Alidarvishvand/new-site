# Generated by Django 3.2.20 on 2023-09-18 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230911_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date']},
        ),
    ]
