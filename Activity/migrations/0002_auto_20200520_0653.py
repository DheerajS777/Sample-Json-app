# Generated by Django 2.1.4 on 2020-05-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_data',
            name='Member_id',
            field=models.CharField(max_length=50),
        ),
    ]