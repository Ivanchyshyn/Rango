import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django.settings')

import django
django.setup()

import logging
logging.basicConfig(filename='populate.log', format='%(asctime)s - %(message)s',
                    datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO)

from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
         "url":"http://flask.pocoo.org"}
    ]

    categories = {
        'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages}
    }

    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for data in cat_data['pages']:
            add_page(c, data['title'], data['url'])

    # Logging output of the created categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            logging.info(f'- {str(c)} - {str(p)}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(cat_name):
    c = Category.objects.get_or_create(name=cat_name)[0]
    c.save()
    return c

if __name__ == '__main__':
    logging.info('Starting Rango population script...')
    populate()
