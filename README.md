# una_health_challenge

To run the server: 
```
python manage.py runserver
```

To run the tests:
```
pytest
```

The pytest module will auto-discover the tests

To import user data, you can use the management command:
```
python manage.py import_glucose_levels_csv [filename]
```

The file can be anywhere on the computer, but must have the format `[uuid].csv`
where uuid corresponds to a valid uuid, and which is the user ID in the database.
If the user id is a valid uuid, and is not found in the database, then it will 
create a user with the uuid of the filename.
