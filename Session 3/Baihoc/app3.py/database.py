import pymongo

client = pymongo.MongoClient("mongodb+srv://trung:Km8WDQLQLUweMzF5@cluster0-hysgg.mongodb.net/test?retryWrites=true")
db = client.test

# # db.foods.save({'name':'com rang','price':'30'})
# db.food.insert_one({'food':'com rang','price':'60k'})
# print(list(db.food.find({})))
# db.food.update_one({'food':'com rang'},{'$set':{'price':100}})
# db.food.delete_one({'food':'com rang'})


def add_food(food,price) :
  db.food.insert_one({'food':food ,'price' :price }) #2 ẩn truyền vào 

def get_all() :
    return list(db.food.find({}))

def get_food_by_name(name):
    return db.food.find_one('com rang')

def update(name,price):
  db.food.update_one({'food':name},{'$set':{'price':price}})
