import csv
import datetime as dt
import pathlib
import uuid

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from glucose_levels.models import GlucoseLevel


def verify_csv_file(suffix):
    if not suffix == ".csv":
        raise CSVValidationError()


def verify_user_uuid(user_uuid):
    if not uuid.UUID(str(user_uuid)):
        raise UserUUIDValidationError()


class CSVValidationError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = "File is not a csv file"


class UserUUIDValidationError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = "Filename does not contain valid user UUID"


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


