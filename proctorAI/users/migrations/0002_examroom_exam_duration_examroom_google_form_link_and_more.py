# Generated by Django 5.1.1 on 2024-10-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examroom',
            name='exam_duration',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AddField(
            model_name='examroom',
            name='google_form_link',
            field=models.URLField(default='google.com'),
        ),
        migrations.AddField(
            model_name='examroom',
            name='link_open_duration',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
