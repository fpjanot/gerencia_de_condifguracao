from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados com uma lista
inventory = []

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    item_quantity = request.form['item_quantity']
    if item_name and item_quantity:
        inventory.append({'name': item_name, 'quantity': item_quantity})
    return redirect(url_for('index'))

@app.route('/delete/<int:item_index>', methods=['POST'])
def delete_item(item_index):
    if 0 <= item_index < len(inventory):
        del inventory[item_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
