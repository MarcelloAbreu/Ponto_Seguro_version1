# Generated by Django 4.1.7 on 2023-05-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_users_superior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='codToken',
            field=models.CharField(max_length=255),
        ),
    ]
