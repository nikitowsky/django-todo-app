from django.test import TestCase
from django.core.exceptions import ValidationError

from core.models import Todo


class TodoModelTestCase(TestCase):
    def test_create_todo_without_title(self):
        """
        Cannot create a todo item without name,
        should throw an validation error
        """

        todo = Todo()

        self.assertRaises(ValidationError, todo.save)
