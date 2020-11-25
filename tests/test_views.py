from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_A_products_json(self):
        print('test_products_json')
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_B_get_one_product_json(self):
        print('test_get_one_product_json')
        response = self.client.get("/api/v1/products/1")
        product = response.json

        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 1)

    def test_C_del_unknown_product(self):
        print('test_del_unknown_product')
        response = self.client.delete("/api/v1/products/13")
        self.assertEqual(response.status_code, 204)

    def test_D_del_known_product(self):
        print('test_del_known_product')
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code, 200)


