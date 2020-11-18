from rest_framework.test import APITestCase

from store.models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count()
        # create new product
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome product',
            'price': '123.45',
        }
        response = self.client.post('/api/v1/products/new', product_attrs)
        # if we cannot create a new product
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Product.objects.count(),
            # checking that there is one more product
            initial_product_count + 1,
        )
        for attr, expected_value in product_attrs.items():
            # checking that the values are correct
            self.assertEqual(response.data[attr], expected_value)

        #     checking custom fields
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(
            response.data['current_price'],
            float(product_attrs['price']),
        )


class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().id
        # delete product
        self.client.delete('/api/v1/products/{}/'.format(product_id))
        # there is one less product in the DB
        self.assertEqual(
            Product.objects.count(),
            initial_product_count - 1,
        )
        # cannot retrieve product
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id,
        )
