# Generated by Django 2.1.7 on 2019-05-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_Can', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
