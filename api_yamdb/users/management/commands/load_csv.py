import csv

from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда загрузки данных из csv в базу данных User"""

    help = ('Добавить данные из csv в базу данных User'
            'получает параметра path - путь к csv файлу'
            'path пишем в ковычках')

    def add_arguments(self, parser):
        print(parser)
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path_file = options['path']
        file = open(path_file)
        reader = csv.DictReader(file)
        User.objects.bulk_create(
            [User(**{k: v for k, v in data.items()}) for data in reader])
        file.close()
        self.stdout.write(self.style.SUCCESS('Successfully added records!'))
