# Generated by Django 3.2.18 on 2024-03-12 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='created_by',
        ),
    ]