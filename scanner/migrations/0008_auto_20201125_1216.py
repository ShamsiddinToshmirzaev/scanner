# Generated by Django 3.1.3 on 2020-11-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0007_auto_20201125_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='ip',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
