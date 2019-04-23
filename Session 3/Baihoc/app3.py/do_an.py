#Km8WDQLQLUweMzF5
from flask import Flask, render_template, request 

app = Flask(__name__)
from database import get_all , add_food ,get_food_by_name,update\


# @app.route('/food_edit/<name>')
# def edit_food(name):
#   food = get_food_by_name(name)
#   return render_template('food_edit.html',food=food)

@app.route('/food_edit/<name>',method=['POST'] )
def edit_food(name):
  food = get_food_by_name(name)
  return render_template('food_edit.html',food=food)



@app.route('/',methods=['POST'])
def post_food():
  gia_tien = request.form.get('gia')
  food_name = request.form.get('ten_mon')
  photo = request.form.get('img')
  add_food(food_name,gia_tien)

  get_all()
  return  render_template('food.html',data=get_all()) #redirect(url_for('get_food'))



@app.route('/')
def get_food():
  return render_template('food.html',data=get_all())

# @app.route('/')
# def get_food():
#   return render_template('food.html',data=foods)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 