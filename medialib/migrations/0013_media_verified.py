# Generated by Django 4.1.3 on 2022-11-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialib', '0012_rename_reference_creator_description_creator_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]