foods = [ 
      {'food':'com rang','price':'30k','img':'https://ameovat.com/wp-content/uploads/2016/05/cach-lam-com-chien-duong-chau-600x481.jpg?fbclid=IwAR1ieNbYUc7gtkBOvT4fRDTp5zg08yVWF22urE04z1Ff_1D_VIPRup87eE0'},
      {'food':'ga ran','price':'160k'}

]
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('vd.html',data = foods)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 