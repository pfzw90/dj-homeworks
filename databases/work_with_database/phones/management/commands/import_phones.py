import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                Phone(id=int(line[0]), name=line[1], price=int(line[3]), image=line[2], release_date=line[4],
                      lte_exists=bool(line[5]), slug=slugify(line[1], allow_unicode=False)).save()

