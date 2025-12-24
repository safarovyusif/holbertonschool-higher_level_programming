from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        try:
            data = read_json()
        except Exception:
            return render_template('product_display.html', error_msg="Error reading JSON")
    elif source == 'csv':
        try:
            data = read_csv()
        except Exception:
            return render_template('product_display.html', error_msg="Error reading CSV")
    else:
        return render_template('product_display.html', error_msg="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]
            if not data:
                return render_template('product_display.html', error_msg="Product not found")
        except ValueError:
             return render_template('product_display.html', error_msg="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
