# Generated by Django 2.1.4 on 2020-02-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0005_comment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
