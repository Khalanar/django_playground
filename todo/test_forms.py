from django.test import TestCase
from .forms import ItemForm


# Create your tests here.
class TestItemForm(TestCase):
    """s"""
    def test_item_name_is_required(self):
        """ds"""
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """ds"""
        form = ItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid())

    def test_forms_are_explicit_in_form_metaclass(self):
        """ds"""
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
