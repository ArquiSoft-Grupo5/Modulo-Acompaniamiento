# Generated by Django 3.2.6 on 2022-04-06 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreAnalisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(blank=True, default=None, null=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('estudiante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiante')),
            ],
        ),
    ]
