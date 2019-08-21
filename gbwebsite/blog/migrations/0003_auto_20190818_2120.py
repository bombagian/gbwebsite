# Generated by Django 2.2.4 on 2019-08-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage_date article published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='Date article published',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='Date published',
            field=models.DateField(blank=True, null=True, verbose_name='Date article published'),
        ),
    ]