from flask import Flask, render_template,request,url_for
app = Flask(__name__)

listfood = [
    {
        'food':'com rang',
        'price': '50k'
    },
    {
        'food':'ga ran',
        'price':'160k'
    }
]


@app.route('/')
def post():
    newfood = request.form.get()
   pass

@app.route('/')
def index():
     return render_template('food.html',foods=listfood)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 