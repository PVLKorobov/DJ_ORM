from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser
from django.template.defaultfilters import slugify
from phones.models import Phone

import csv


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args: csv.Any, **options: csv.Any) -> str | None:
        with open('phones.csv', 'r', encoding='utf8') as file:
            data = csv.DictReader(file, delimiter=';')
            for row in data:
                try:
                    Phone.objects.create(
                        id = row['id'],
                        name = row['name'],
                        slug = slugify(row['name']),
                        price = row['price'],
                        image = row['image'],
                        release_date = row['release_date'],
                        lte_exists = row['lte_exists']
                        
                    )
                except:
                    raise CommandError(f'Item with id={row["id"]} already exists')
        return super().handle(*args, **options)