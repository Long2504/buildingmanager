# Generated by Django 4.0.3 on 2022-06-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('status', models.TextField(max_length=255)),
                ('area', models.IntegerField()),
                ('deleted_flag', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='static/image/floor/')),
            ],
        ),
    ]
