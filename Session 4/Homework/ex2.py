from flask import Flask, render_template , redirect , request,url_for

from dbase import get_all
app = Flask(__name__)

@app.route('/')
def get_food() :

    return render_template('list.html',data=get_all())

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 