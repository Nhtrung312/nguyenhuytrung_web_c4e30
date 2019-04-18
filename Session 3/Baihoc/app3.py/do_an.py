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

# @app.route('/')
# def insert_img():
#     img = request.form.get('img')
#     food_name2 = request.form.get('tenmon')
#     a = 0
#     for v in foods :
#       if food_name2 == v['food'] :
#         a = 1 
#     if a==1 :
#       v['anh'] == img 
    
#       return  render_template('food.html',data=foods) 
#     else :
#       return render_template('food.html',data=foods) 
    


@app.route('/')
def get_food():
  return render_template('food.html',data=foods)

# @app.route('/')
# def get_food():
#   return render_template('food.html',data=foods)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 