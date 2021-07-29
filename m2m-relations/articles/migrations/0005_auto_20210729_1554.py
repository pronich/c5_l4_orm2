# Generated by Django 3.2.5 on 2021-07-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.TextField(max_length=100, verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='taglink',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]