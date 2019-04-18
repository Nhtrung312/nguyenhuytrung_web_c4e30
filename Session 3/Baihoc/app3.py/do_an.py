from flask import Flask, render_template, request 

app = Flask(__name__)
foods = [ 
      {'food':'com rang','price':'30k'},
      {'food':'ga ran','price':'160k'}

]


@app.route('/',methods=['POST'])
def post_food():
  gia_tien = request.form.get('gia')
  food_name = request.form.get('ten_mon')
  photo = request.form.get('img')
  food1 = {
    'food':food_name,
    'price': gia_tien,
    'anh': photo
   }

  foods.append(food1)
  return  render_template('food.html',data=foods) #redirect(url_for('get_food'))



@app.route('/')
def get_food():
  return render_template('food.html',data=foods)

# @app.route('/')
# def get_food():
#   return render_template('food.html',data=foods)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 