# Generated by Django 4.2.5 on 2024-03-25 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.FloatField(blank=True, null=True)),
                ('test2', models.FloatField(blank=True, null=True)),
                ('test3', models.FloatField(blank=True, null=True)),
                ('test4', models.FloatField(blank=True, null=True)),
                ('test5', models.FloatField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.student')),
            ],
        ),
    ]
