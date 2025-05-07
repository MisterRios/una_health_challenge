import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


def verify_csv_file(filename):
    if filename.endswith(".csv"):
        return True
    return False

class CSVValidationError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = "File is not a csv file"


class Command(BaseCommand):
    help = "imports glucose level telemetry from csv file"

    def add_arguments(self, parser):
        parser.add_argument("filenames", nargs="+", type=str)

    def handle(self, *args, **options):
        for csv_filename in options["filenames"]:
            breakpoint()
            if not verify_csv_file(csv_filename):
                raise CSVValidationError()

            with open(csv_filename) as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    print(row)


