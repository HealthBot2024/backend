# Generated by Django 4.2.3 on 2025-02-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0003_alter_user_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='drives',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
