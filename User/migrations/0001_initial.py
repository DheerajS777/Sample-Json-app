# Generated by Django 2.1.4 on 2020-05-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=150)),
                ('No_of_WorkDaysPerWeek', models.IntegerField()),
            ],
        ),
    ]