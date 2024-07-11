# Generated by Django 5.0.6 on 2024-06-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DLP', '0004_datagazedlp_about_en_datagazedlp_about_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='about_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='about_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='about_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]