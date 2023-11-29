from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/amazon'
db = SQLAlchemy(app)
class Contents(db.Model):
    item_type = db.Column(db.String(80), nullable=False)
    item_details = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_source = db.Column(db.String(1500), nullable=False)
    item_serial_number = db.Column(db.Integer, nullable=False)
    item_disc = db.Column(db.String(80), nullable=False, primary_key=True)

class Cart(db.Model):
    item_serial_number = db.Column(db.Integer, nullable=False, primary_key=True)
 
@app.route('/indexx' ,methods=['GET','POST'])
def index():
    
    global table2_data
    table2_data = Contents.query.all()

    if(request.method=='POST'):
        item_serial_number=request.form.get('item_serial_number')
        entry=Cart(item_serial_number=item_serial_number)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html', table2_data=table2_data)


@app.route('/cart')
def cart():
    table2_data = Contents.query.all()
    table3=Cart.query.all()
    db.session.query(Cart).delete()
    db.session.commit()
    return render_template('cart.html',table3=table3,table2_data=table2_data)
 
 
if __name__ == "__main__":
    app.run(debug=True)
