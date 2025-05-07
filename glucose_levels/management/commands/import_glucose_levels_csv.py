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
            file_path = pathlib.PurePath(csv_filename)
            user_uuid = file_path.stem
            file_suffix = file_path.suffix

            verify_user_uuid(user_uuid)
            verify_csv_file(file_suffix)
            user_model = get_user_model()
            user, created = user_model.objects.get_or_create(id=user_uuid, username=user_uuid)

            with open(csv_filename) as csv_file:
                reader = csv.reader(csv_file)
                # skip first three rows of header information
                next(reader)
                next(reader)
                next(reader)

                for row in reader:
                    datetime_object = dt.datetime.strptime(row[2], "%d-%m-%Y %H:%M")
                    device_timestamp = datetime_object.strftime( "%Y-%m-%d %H:%M")
                    row = [column or None for column in row]

                    GlucoseLevel.objects.get_or_create(
                        user=user,
                        device=row[0],
                        serial_number=row[1],
                        device_timestamp=device_timestamp,
                        record_type=row[3],
                        glucose_value_trend=row[4],
                        glucose_scan=row[5],
                        nonnumeric_rapid_acting_insulin=row[6],
                        rapid_acting_insulin=row[7],
                        nonnumeric_food_data=row[8],
                        carbohydrates=row[9],
                        carbohydrate_servings=row[10],
                        nonnumeric_slow_release_insulin=row[11],
                        slow_release_insulin=row[12],
                        notes=row[13],
                        glucose_test_strip=row[14],
                        ketone=row[15],
                        mealtime_insulin=row[16],
                        correction_insulin=row[17],
                        user_changed_insulin=row[18],
                    )
