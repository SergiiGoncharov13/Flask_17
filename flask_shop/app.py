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
        

@app.route('/order/<int:product_id>', methods=['POST', 'GET'])
def order(product_id):
    with Session() as session:
        product = session.query(Product).get(product_id)
        if not product:
            return 'Boots not found', 404

        if request.method == 'POST':
            phone = request.form['phone']
            email = request.form['email']

            new_order =Orders(phone=phone, email=email, product_id=product_id)
            session.add(new_order)
            session.commit()

            return redirect(url_for('index'))
        
        return render_template('order.html', product=product)



if __name__ == '__main__':
    app.run(debug=True, port=8000)


