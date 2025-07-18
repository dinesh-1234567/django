# Generated by Django 5.2.4 on 2025-07-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2025-12-31'),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='M', max_length=1),
        ),
    ]
