# Generated by Django 4.2.5 on 2024-03-23 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_alter_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.subject'),
        ),
    ]
