# Generated by Django 5.1.1 on 2024-09-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognews',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание на рус'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='message_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Сообщение на рус'),
        ),
    ]