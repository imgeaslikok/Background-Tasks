# Background-Tasks
Using django-background-tasks library for long running processes

Django-background-tasks can be used for creating the task functions and registering them with the scheduler or setup a cron task (or long running process) to execute the tasks.

**Installation**

```
pip install django-background-tasks
```

After installing the library, it must be added the INSTALLED_APPS.

```
INSTALLED_APPS = (
    # ...
    'background_task',
    # ...
)
```
And then, should be made migrate.
```
python manage.py migrate
```
After the background task structure is set up as in this sample project, the following command should be run.
```
python manage.py process_tasks
```
In localhost, this command can be run manually in the background, but when you want to deploy the project, crontab, etc. should be used.

About more, here is the documentation: https://django-background-tasks.readthedocs.io/en/latest/
