# Generated by Django 4.1.7 on 2023-05-27 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_histregistro_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='histregistro',
            name='tipo',
        ),
    ]
