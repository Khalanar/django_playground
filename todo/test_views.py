from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    """ds"""

    def test_get_todo_list(self):
        """ds"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item(self):
        """ds"""
        response = self.client.get('/add_item')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item(self):
        """ds"""
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ds"""
        response = self.client.post('/add_item', {'name': 'Test Adding Item'})
        self.assertRedirects(response, '/')

    def test_can_remove_item(self):
        """ds"""
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.get(f'/remove/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
    
    def test_can_toggle_item(self):
        """ds"""
        item = Item.objects.create(name="Test Todo Item", done=True)
        response = self.client.get(f'/toggle_complete/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        """s"""
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')

