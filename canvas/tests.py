from django.test import TestCase

# Create your tests here.
import unittest

from canvas.models import *




class TestStringMethods(unittest.TestCase):
    def test_Create_User(self):
        admin=CanvasUser()
        admin.password="Welcome1"
        admin.user_type=1
        admin.user_name="rock"
        CanvasUser.objects.create(admin)

if __name__ == '__main__':
    unittest.main()