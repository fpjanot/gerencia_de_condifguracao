from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Simulação de banco de dados com uma lista
inventory = []

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    item_quantity = request.form['item_quantity']
    item_price = request.form['item_price']
    item_description = request.form['item_description']
    if item_name and item_quantity and item_price and item_description:
        inventory.append({
            'name': item_name,
            'quantity': item_quantity,
            'price': item_price,
            'description': item_description
        })
    return redirect(url_for('index'))

@app.route('/delete/<int:item_index>', methods=['POST'])
def delete_item(item_index):
    if 0 <= item_index < len(inventory):
        del inventory[item_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
