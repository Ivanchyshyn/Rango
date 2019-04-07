from django.test import TestCase

from .models import Category, Page

class CategoryModelTests(TestCase):

    def setUp(self):
        try:
            from populate_rango import populate
            populate()
        except ImportError:
            print("The module populate_rango does not exist")
        except NameError:
            print("The function populate() does not exist or is not correct")
        except Exception as ex:
            print("Unexpected exception in populate() function - %s" % ex)

    def get_category(self, name):
        try:
            categories = Category.objects.get(name=name)
            return categories
        except Category.DoesNotExist:
            return None

    def test_added_python(self):
        self.assertIsNotNone(self.get_category("Python"))

    def test_python_views(self):
        cat = self.get_category('Python')
        self.assertEqual(cat.views, 128)

    def test_python_likes(self):
        cat = self.get_category('Python')
        self.assertEqual(cat.likes, 64)
