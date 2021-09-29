from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_message_is_required(self):
        form = CommentForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_fields_are_explicit_in_forms_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('message',))
