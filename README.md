# RestaSoft
SW Restaurant 
------------------

## TEAM MEMBERS

### Front-end
* Mario David González Contreras
* Luis Fernando Hernández Piñón 

### Back-end
* Alejandro Pérez Pizano
* Brenda Liliana Gutierrez Ramirez
------------------

## Supported browsers


The goal of the site is to target various levels of browsers, depending on
their ability to use the technologies in use on the site, such as HTML5, CSS3,
SVG, webfonts.

We're following `Mozilla's example <https://wiki.mozilla.org/Support/Browser_Support>`_
when it comes to categorizing browser support.

- Desktop browsers, except as noted below, are **A grade**, meaning that
  everything needs to work.

- IE < 11 is **not supported** (based on Microsoft's support).

- Mobile browsers should be considered **B grade** as well.
  Mobile Safari, Firefox on Android and the Android Browser should support
  the responsive styles as much as possible but some degredation can't be
  prevented due to the limited screen size and other platform restrictions.

## File locations


Static files such as CSS, JavaScript or image files can be found in the
``RestaSoft/static`` subdirectory.

Templates can be found in the ``Restasoft/templates`` subdirectory.


## 🚀 Features


- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)


## 📖 Installation
DjangoX can be installed via Pip, Pipenv, or Docker depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/wsvincent/djangox.git
$ cd djangox
```

### Pip

```
$ python3 -m venv djangox
$ source djangox/bin/activate
(djangox) $ pip install -r requirements.txt
(djangox) $ python manage.py migrate
(djangox) $ python manage.py createsuperuser
(djangox) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

## Setup

```
# Run Migrations
(djangox) $ python manage.py migrate

# Create a Superuser
(djangox) $ python manage.py createsuperuser

# Confirm everything is working:
(djangox) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

----
