import csv

from django.apps import apps

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Команда загрузки данных из csv в базу данных User"""

    help = ('Добавить данные из csv в базу данных User.'
            'Параметры:'
            'path - путь к csv файлу, пишем в ковычках'
            'app_name - имя приложения'
            'model_name - имя модели')

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        parser.add_argument('app_name', type=str)
        parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        # получим модель
        model = apps.get_model(
            app_label=options['app_name'],
            model_name=options['model_name'],
            require_ready=False)
        path_file = options['path']
        file = open(path_file)
        reader = csv.DictReader(file)
        model.objects.bulk_create(
            [model(**{k: v for k, v in data.items()}) for data in reader])
        file.close()
        self.stdout.write(self.style.SUCCESS('Successfully added records!'))
