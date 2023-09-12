# Django project

## Software needed:

- python
- pip3
- django
- db browser for SQLlite (optional)

## spin up project and app:

`django-admin startproject lawncare`

`python3 manage.py startapp fertilizer`

`python3 manage.py runserver`

## Shell commands to instantiate the model objects and then save to db

`>>> f = Fertilizer(name='Milorganite', bag_weight=36, bag_coverage=2500, percent_N=6, percent_P=4, percent_X=0)

> > > Fertilizer.objects.all()
> > > <QuerySet []>
> > > f.save()
> > > Fertilizer.objects.all()
> > > <QuerySet [<Fertilizer: Fertilizer object (1)>]>
> > > Fertilizer.objects.get(pk=1)
> > > <Fertilizer: Fertilizer object (1)>
> > > f.name
> > > 'Milorganite'
> > > f
> > > <Fertilizer: Fertilizer object (1)>
> > > f.name
> > > 'Milorganite'
> > > Fertilizer.objects.all()
> > > <QuerySet [<Fertilizer: Fertilizer object (1)>]>
> > > Fertilizer.objects.all()
> > > <QuerySet [<Fertilizer: Fertilizer object (1)>]>
> > > quit()
> > > markl@MyOfficeDesktop:/mnt/c/Users/mark\_/GIT/djangoTutorial/lawncare$ python3 manage.py shell
> > > Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
> > > Type "help", "copyright", "credits" or "license" for more information.
> > > (InteractiveConsole)
> > > from fertilizer.models import Fertilizer
> > > Fertilizer.objects.all()
> > > <QuerySet [<Fertilizer: Milorganite 6.00-4.00-0.00>]>`

## Admin Portal

`markl@MyOfficeDesktop:/mnt/c/Users/mark_/GIT/djangoTutorial/lawncare$ python3 manage.py createsuperuser
Username (leave blank to use 'markl'): markladmin
Email address: mark_landry2@yahoo.com
Password: 
Password (again): 
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.`
