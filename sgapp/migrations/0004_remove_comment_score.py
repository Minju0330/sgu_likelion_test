# Generated by Django 2.1.4 on 2020-02-21 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0003_comment_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='score',
        ),
    ]
