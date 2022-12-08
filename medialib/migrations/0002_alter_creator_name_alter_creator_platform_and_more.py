# Generated by Django 4.1.3 on 2022-11-16 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medialib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='creator',
            name='platform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medialib.platform'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='reference',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='creator',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='media',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]