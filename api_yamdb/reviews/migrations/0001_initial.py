# Generated by Django 2.2.16 on 2021-08-14 15:45

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(help_text='Введите текст комментария', verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Напишите отзыв', verbose_name='Отзыв')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(help_text='Поставьте оценку произведению от 1 до 10', validators=[reviews.validators.score_validation])),
            ],
        ),
    ]