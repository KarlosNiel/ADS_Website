# Generated by Django 5.2 on 2025-04-29 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_app', '0004_documentacao_extensao_postnoticia_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensao',
            name='tipo',
            field=models.CharField(choices=[('Atual', 'Atual'), ('Futura', 'Futura')], default='Atual', max_length=10),
        ),
    ]
