from flask import Flask, render_template, request, redirect, url_for

from databases import Session, Product, Orders

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    with Session() as session:
        all_produdts = session.query(Product).all()
    
    return render_template('products.html', products=all_produdts)
        



if __name__ == '__main__':
    app.run(debug=True, port=8000)


