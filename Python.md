# Python Pots #
---

Windows Command Line

- Choosing between versions of Python
	- py -2 (version 2)
	- py -3 (version 3)

    col2 = [row[1] for row in M]
    
    G = (sum(row) for row in M)

Nesting

    rec = {'name': {'first': 'Bob', 'last': 'Smith'},
           'jobs': ['dev', 'mgr'],
           'age':  40.5}

    
###Tuples



###Files



###Other Core Types


#### Useful Tips

@ = decorator

python3 -m venv venv

python3 is the command

source {virtual env}/bin/activate

pip install "Django<1.9"

mutable = value can change
immutable = value cannot change

env/bin/python manage.py runserver 0.0.0.0:8000

app is a self contained module that lives in your Django project

#### Generate a new app

	django-admin startapp <nameofapp>

#### Django-debug-toolbar

	pip install django-debug-toolbar

	pip freeze (shows what's installed)

#### Other Django commands
---

python manage.py makemigrations - creates migration file

python manage.py migrate - applys migrations

python manage.py shell - Shell

python manage.py createsuperuser (creates user)

mybook = (put in book)

mybook.save()

**Use dot notation to access any attribute**

book.title i.e book.review

Book.objects.all() // Retrieve all books

from books.models import Book

**Filter query**

Book.objects.filter(attribute="whatever)

Book.objects.filter(attribute__contains="whatever)

Book.objects.filter(attribute__startswith="whatever)

**Django Admin**


**HMM no exercise files**

---
pip install flask
10/11/2014 9:48:10 PM 

---