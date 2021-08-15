import csv
import os

from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    '''Cоздаем команду для manage.py для добавления записи из csv файла в БД
    принимает один аргумент - имя csv файла.'''

    help = ('Add records from csv file in db - '
            'addrecords <name csv file>')

    def add_arguments(self, parser):
        parser.add_argument('csv_name', nargs='+')

    def handle(self, *args, **options):
        path_file = f'd:\\Dev\\api_yamdb\\api_yamdb\\static\\data\\{options["csv_name"]}'
        file = open(path_file)
        read_file = csv.reader(file)
        for record in read_file:
            User.objects.create(
                username=record[1], email=record[2], role=record[3], bio=record[4], first_name=record[5], last_name=record[6])
        file.close()
