# Generated by Django 5.0.6 on 2024-05-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='stack',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
