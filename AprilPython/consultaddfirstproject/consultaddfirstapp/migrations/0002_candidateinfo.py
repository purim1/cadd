# Generated by Django 2.1.7 on 2019-05-16 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultaddfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CanID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consultaddfirstapp.Candidate')),
            ],
        ),
    ]