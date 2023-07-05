# Generated by Django 4.1.7 on 2023-04-09 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_escala_domingo_escala_quarta_escala_quinta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escala',
            old_name='horaEntM',
            new_name='horEnt1',
        ),
        migrations.RenameField(
            model_name='escala',
            old_name='horaEntV',
            new_name='horEnt3',
        ),
        migrations.RenameField(
            model_name='escala',
            old_name='horaSaiM',
            new_name='horSai2',
        ),
        migrations.RenameField(
            model_name='escala',
            old_name='horaSaiV',
            new_name='horSai4',
        ),
        migrations.RenameField(
            model_name='histregistro',
            old_name='horaEntM',
            new_name='horEnt1',
        ),
        migrations.RenameField(
            model_name='histregistro',
            old_name='horaEntV',
            new_name='horEnt3',
        ),
        migrations.RenameField(
            model_name='histregistro',
            old_name='horaSaiM',
            new_name='horSai2',
        ),
        migrations.RenameField(
            model_name='histregistro',
            old_name='horaSaiV',
            new_name='horSai4',
        ),
        migrations.CreateModel(
            name='HoraExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataLib', models.DateField(blank=True, null=True)),
                ('horEnt1', models.TimeField(blank=True, null=True)),
                ('horSai2', models.TimeField(blank=True, null=True)),
                ('horEnt3', models.TimeField(blank=True, null=True)),
                ('horSai4', models.TimeField(blank=True, null=True)),
                ('userExtra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hora Extra',
                'verbose_name_plural': 'Horas Extras',
                'db_table': 'horaextra',
            },
        ),
    ]