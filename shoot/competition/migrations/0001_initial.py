# Generated by Django 2.0 on 2018-03-31 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_id', models.CharField(max_length=10, verbose_name='Id')),
                ('competition_name', models.CharField(max_length=100, verbose_name='Competition')),
                ('start_from', models.DateField()),
                ('end_on', models.DateField()),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(max_length=6, null=True)),
                ('match_detail', models.CharField(max_length=100, null=True)),
                ('targets', models.IntegerField(null=True)),
                ('fees', models.IntegerField(null=True)),
                ('competition_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='competition.Competitions')),
            ],
        ),
    ]