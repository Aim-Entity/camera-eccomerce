# Generated by Django 3.0.7 on 2021-01-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210108_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='aspect_ratio',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]