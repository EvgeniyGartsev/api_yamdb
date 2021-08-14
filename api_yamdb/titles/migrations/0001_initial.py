# Generated by Django 2.2.16 on 2021-08-12 13:23

from django.db import migrations, models
import django.db.models.deletion
import titles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Укажите название для категории', max_length=256, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Задайте уникальный URL адрес категории. Используйте только латиницу, цифры, дефисы и знаки подчёркивания', unique=True, verbose_name='URL категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Укажите название жанра', max_length=256, verbose_name='Название жанра')),
                ('slug', models.SlugField(help_text='Задайте уникальный URL адрес жанра. Используйте только латиницу, цифры, дефисы и знаки подчёркивания', unique=True, verbose_name='URL жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Укажите название произведения', max_length=256, verbose_name='Название произведения')),
                ('year', models.PositiveSmallIntegerField(help_text='Задайте год выпуска', validators=[titles.validators.year_validation], verbose_name='Год выпуска')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='titles.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(blank=True, related_name='titles', to='titles.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('-year',),
            },
        ),
    ]
