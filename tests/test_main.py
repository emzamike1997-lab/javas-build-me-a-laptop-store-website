### === test_models.py ===
```python
import unittest
from unittest.mock import Mock
from your_laptop_store.models import Laptop, Brand, Category

class TestLaptopModel(unittest.TestCase):
    def test_laptop_creation(self):
        laptop = Laptop(name='Test Laptop', price=1000, brand='Test Brand', category='Test Category')
        self.assertEqual(laptop.name, 'Test Laptop')
        self.assertEqual(laptop.price, 1000)
        self.assertEqual(laptop.brand, 'Test Brand')
        self.assertEqual(laptop.category, 'Test Category')

    def test_brand_creation(self):
        brand = Brand(name='Test Brand')
        self.assertEqual(brand.name, 'Test Brand')

    def test_category_creation(self):
        category = Category(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

class TestLaptopRelationships(unittest.TestCase):
    def test_laptop_brand_relationship(self):
        brand = Brand(name='Test Brand')
        laptop = Laptop(name='Test Laptop', price=1000, brand=brand)
        self.assertEqual(laptop.brand, brand)

    def test_laptop_category_relationship(self):
        category = Category(name='Test Category')
        laptop = Laptop(name='Test Laptop', price=1000, category=category)
        self.assertEqual(laptop.category, category)

if __name__ == '__main__':
    unittest.main()
```

### === test_views.py ===
```python
import unittest
from django.test import TestCase, Client
from your_laptop_store.views import LaptopListView, LaptopDetailView

class TestLaptopListView(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_laptop_list_view(self):
        response = self.client.get('/laptops/')
        self.assertEqual(response.status_code, 200)

    def test_laptop_list_view_context(self):
        response = self.client.get('/laptops/')
        self.assertIn('laptop_list', response.context)

class TestLaptopDetailView(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_laptop_detail_view(self):
        response = self.client.get('/laptops/1/')
        self.assertEqual(response.status_code, 200)

    def test_laptop_detail_view_context(self):
        response = self.client.get('/laptops/1/')
        self.assertIn('laptop', response.context)

if __name__ == '__main__':
    unittest.main()
```

### === test_templates.py ===
```python
import unittest
from django.test import TestCase
from your_laptop_store.templates import laptop_list_template, laptop_detail_template

class TestLaptopListTemplate(unittest.TestCase):
    def test_laptop_list_template(self):
        template = laptop_list_template()
        self.assertIn('laptop_list', template.context)

    def test_laptop_list_template_rendering(self):
        template = laptop_list_template()
        rendered_template = template.render()
        self.assertIn('Laptop List', rendered_template)

class TestLaptopDetailTemplate(unittest.TestCase):
    def test_laptop_detail_template(self):
        template = laptop_detail_template()
        self.assertIn('laptop', template.context)

    def test_laptop_detail_template_rendering(self):
        template = laptop_detail_template()
        rendered_template = template.render()
        self.assertIn('Laptop Details', rendered_template)

if __name__ == '__main__':
    unittest.main()
```

### === test_forms.py ===
```python
import unittest
from django.test import TestCase
from your_laptop_store.forms import LaptopForm

class TestLaptopForm(unittest.TestCase):
    def test_laptop_form(self):
        form_data = {'name': 'Test Laptop', 'price': 1000, 'brand': 'Test Brand', 'category': 'Test Category'}
        form = LaptopForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_laptop_form_invalid(self):
        form_data = {'name': '', 'price': 1000, 'brand': 'Test Brand', 'category': 'Test Category'}
        form = LaptopForm(data=form_data)
        self.assertFalse(form.is_valid())

if __name__ == '__main__':
    unittest.main()
```

### === test_urls.py ===
```python
import unittest
from django.test import TestCase
from django.urls import reverse

class TestLaptopUrls(unittest.TestCase):
    def test_laptop_list_url(self):
        url = reverse('laptop_list')
        self.assertEqual(url, '/laptops/')

    def test_laptop_detail_url(self):
        url = reverse('laptop_detail', args=[1])
        self.assertEqual(url, '/laptops/1/')

if __name__ == '__main__':
    unittest.main()
```

### === test_integration.py ===
```python
import unittest
from django.test import TestCase, Client
from your_laptop_store.models import Laptop

class TestLaptopIntegration(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.laptop = Laptop.objects.create(name='Test Laptop', price=1000, brand='Test Brand', category='Test Category')

    def test_laptop_list_view_integration(self):
        response = self.client.get('/laptops/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.laptop.name, response.content.decode('utf-8'))

    def test_laptop_detail_view_integration(self):
        response = self.client.get('/laptops/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.laptop.name, response.content.decode('utf-8'))

    def test_laptop_creation_integration(self):
        form_data = {'name': 'New Laptop', 'price': 2000, 'brand': 'New Brand', 'category': 'New Category'}
        response = self.client.post('/laptops/', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Laptop.objects.count(), 2)

if __name__ == '__main__':
    unittest.main()
```

### === test_api.py ===
```python
import unittest
from django.test import TestCase, Client
from rest_framework import status
from your_laptop_store.serializers import LaptopSerializer
from your_laptop_store.models import Laptop

class TestLaptopApi(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.laptop = Laptop.objects.create(name='Test Laptop', price=1000, brand='Test Brand', category='Test Category')

    def test_laptop_list_api(self):
        response = self.client.get('/api/laptops/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.laptop.name, response.content.decode('utf-8'))

    def test_laptop_detail_api(self):
        response = self.client.get('/api/laptops/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.laptop.name, response.content.decode('utf-8'))

    def test_laptop_creation_api(self):
        form_data = {'name': 'New Laptop', 'price': 2000, 'brand': 'New Brand', 'category': 'New Category'}
        response = self.client.post('/api/laptops/', data=form_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Laptop.objects.count(), 2)

if __name__ == '__main__':
    unittest.main()
```