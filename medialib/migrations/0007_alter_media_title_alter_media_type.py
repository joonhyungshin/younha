# Generated by Django 4.1.3 on 2022-11-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialib', '0006_alter_media_options_alter_media_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='media',
            name='type',
            field=models.CharField(choices=[('I', 'Image'), ('V', 'Video'), ('A', 'Audio'), ('Y', 'Youtube video')], max_length=1),
        ),
    ]
