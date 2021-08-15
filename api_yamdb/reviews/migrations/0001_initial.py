# Generated by Django 2.2.16 on 2021-08-15 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите текст комментария', verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Напишите отзыв', verbose_name='Отзыв')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(help_text='Поставьте оценку произведению от 1 до 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
    ]
