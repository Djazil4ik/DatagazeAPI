# Generated by Django 5.0.6 on 2024-05-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('URL', models.URLField()),
            ],
        ),
    ]
