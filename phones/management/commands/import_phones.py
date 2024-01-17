import csv

from django.core.management.base import BaseCommand
from phones.models import Mobile
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            dict_collect = {}
            for row in csv_reader:
                print(row)
                if line_count == 0:
                    for key in row:
                        dict_collect[key] = ""
                    line_count += 1
                else:
                    j = 0
                    keys = list(dict_collect.keys())
                    for value in row:
                        dict_collect[keys[j]] = value
                        j += 1
                    phone = Mobile(id_phone=int(dict_collect["id"]), name=dict_collect["name"],
                                  price=int(dict_collect["price"]), image=dict_collect["image"],
                                  release_date=dict_collect["release_date"],
                                  lte_exists=bool(dict_collect["lte_exists"]),
                                   slug=slugify(dict_collect["name"]))
                    phone.save()
