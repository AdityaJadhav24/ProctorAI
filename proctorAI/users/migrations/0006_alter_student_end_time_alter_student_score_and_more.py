# Generated by Django 5.1.1 on 2024-10-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_examroom_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
