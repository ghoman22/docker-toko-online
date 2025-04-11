from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'tokorandom123'

products = [
    {'id': 1, 'name': 'Baju Keren', 'price': 100000},
    {'id': 2, 'name': 'Celana Gaul', 'price': 150000},
    {'id': 3, 'name': 'Topi Kece', 'price': 50000}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    cart_items = [p for p in products if p['id'] in cart]
    total = sum([p['price'] for p in cart_items])
    return render_template('cart.html', cart=cart_items, total=total)

@app.route('/checkout')
def checkout():
    session['cart'] = []
    return "Checkout berhasil! 🎉"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
