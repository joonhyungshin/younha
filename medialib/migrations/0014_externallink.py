# Generated by Django 4.1.3 on 2022-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialib', '0013_media_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('display', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('priority',),
            },
        ),
    ]