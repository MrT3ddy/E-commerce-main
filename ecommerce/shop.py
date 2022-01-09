import functools

from flask import (
    Blueprint,flash,g, redirect, render_template, request,session, url_for
)

from ecommerce.db import get_db

bp = Blueprint('shop', __name__)

#home page lists all product off rip
@bp.route('/')
def home():
    # search up flask documentation blog for listing items on the page, cmd + F for posts to see html for loop

    db = get_db()
    item = db.execute(
        
        'SELECT id,title, detail, price, size, color, quantity'
        ' FROM product'
    ).fetchall()
    db = get_db()
    
    return render_template('shop/home.html',item=item)

# renders product based off href
@bp.route('/<id>')
def product(id):
    db = get_db()
    item = db.execute(
        'SELECT title, detail, price, size, color, quantity'
        ' FROM product WHERE id==?', (id)
    ).fetchall()
    

         
    return render_template('shop/product.html',item=item)



# shopping cart
@bp.route('/cart',methods=('GET', 'POST'))
def cart():
    db = get_db()
    item = db.execute(
        'SELECT title, detail, price, size, color, quantity'
        ' FROM product WHERE id==?', (id)
    ).fetchall()
    if request.method == 'POST':
        size = request.form['size']
        quantity = request.form['quantity']
    
    return render_template('shop/cart.html')