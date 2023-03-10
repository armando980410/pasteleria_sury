# Generated by Django 4.1.7 on 2023-03-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=64)),
                ('imagen', models.TextField()),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField()),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
