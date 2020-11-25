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
    products = list(PRODUCTS.values())

    return  jsonify(products), 200

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def read_one_product(product_id):
    product = PRODUCTS.get(product_id)
    if product is None:
        abort(404)
    return jsonify(product), 200

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_one_product(product_id):
    product = PRODUCTS.pop(product_id, None)
    if product is None:
        abort(404)

    return '', 204

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    body_json = request.get_json()

    new_product_name = body_json.get('name')

    if new_product_name is None:
        abort(422)

    new_product_id = next(IDENTIFIER_GENERATOR)
    new_product = {'id': new_product_id, 'name': new_product_name}

    PRODUCTS[new_product_id] = new_product

    print(PRODUCTS)

    return jsonify(new_product), 201
