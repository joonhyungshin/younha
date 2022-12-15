# Generated by Django 4.1.3 on 2022-12-15 00:56

from django.db import migrations


def move_source(apps, schema_editor):
    Media = apps.get_model('medialib', 'Media')
    MediaSource = apps.get_model('medialib', 'MediaSource')
    for media in Media.objects.all():
        source, _ = MediaSource.objects.get_or_create(url=media.source_url)
        media.source = source
        media.save()


class Migration(migrations.Migration):

    dependencies = [
        ('medialib', '0021_license_mediasource_remove_media_date_type_and_more'),
    ]

    operations = [
        migrations.RunPython(move_source)
    ]