import unittest
from domain.models.student import Student

class TestStringMethods(unittest.TestCase):
    def test_full_name(self):
        first_name = "first"
        last_name = "last"
        middle_name = "middle"

        student = Student(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name
        )

        expected_full_name = first_name + " " + middle_name + " " + last_name
        self.assertEqual(expected_full_name, student.full_name())
