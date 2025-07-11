from flask import Flask, render_template

app = Flask(__name__, template_folder='html_pages')

@app.route('/')
def login():
    return render_template('login.html')  # renamed from index.html

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')

@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/items')
def items():
    return render_template('items.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/coupons')
def coupons():
    return render_template('coupons.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True)