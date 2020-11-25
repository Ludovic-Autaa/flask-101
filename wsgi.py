# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Python in a Nutshell' },
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def read_many_products():
    return  jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:product_id>')
def read_one_product(product_id):
    return jsonify(PRODUCTS[1])

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_one_product(product_id):
    if PRODUCTS.get(product_id) is None:
        return 'unknown product id', 204
    else:
        del PRODUCTS[product_id]
        return f'product {product_id} deleted', 200
