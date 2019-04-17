from flask import Flask, render_template,request,url_for
app = Flask(__name__)


@app.route('/',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'nhtrung312' and password == 'trung312' :
        return render_template('login1.html')
    else : 
        return render_template('login2.html')
    
@app.route('/')
def get():
   return render_template('login.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 