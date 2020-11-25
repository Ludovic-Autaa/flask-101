# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort, request
import itertools

app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Python in a Nutshell' },
}

START_INDEX = len(PRODUCTS) + 1
IDENTIFIER_GENERATOR = itertools.count(START_INDEX)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def read_many_products():
    return  jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def read_one_product(product_id):
    if PRODUCTS.get(product_id) is None:
        return abort(404)
    else:
        return jsonify(PRODUCTS[1]), 200

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_one_product(product_id):
    if PRODUCTS.get(product_id) is None:
        return abort(404)
    else:
        del PRODUCTS[product_id]
        return f'product {product_id} deleted', 204

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    req = request.get_json()

    new_product_id = next(IDENTIFIER_GENERATOR)
    new_product_name = req['name']

    new_product = {'id': new_product_id, 'name': new_product_name}

    PRODUCTS.update(new_product)

    return jsonify(new_product), 201
