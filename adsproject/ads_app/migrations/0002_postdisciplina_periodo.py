# Generated by Django 5.1.7 on 2025-04-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdisciplina',
            name='periodo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
