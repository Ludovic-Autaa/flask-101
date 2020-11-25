# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def read_many_products():
    PRODUCTS = {
        1: { 'id': 1, 'name': 'Skello' },
        2: { 'id': 2, 'name': 'Socialive.tv' },
    }
    return  jsonify(PRODUCTS)
