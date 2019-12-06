from django.test import TestCase
from django.core.exceptions import ValidationError

from core.models import Tag


class TodoModelTestCase(TestCase):
    def test_create_tag_without_title(self):
        """
        Cannot create a tag without name, should throw an validation error
        """

        tag = Tag()

        self.assertRaises(ValidationError, tag.save)
