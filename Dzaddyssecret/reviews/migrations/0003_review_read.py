# Generated by Django 4.0.5 on 2022-06-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]