from flask import Flask, render_template,request,url_for
app = Flask(__name__)

account = [
  {
    'user' : 'trung312',
    'pass': 'trung312'
      },
  {
    'user':'trung123',
    'pass':'trung123'

     },
  {
    'user':'trung321',
    'pass':'trung321'
  }
]

@app.route('/',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ktra = 0
    #ktra đáp án 
    for v in account :
      if username == v['user']  and password == v['pass'] :
        ktra = 1
        

    if ktra==1 :
        return render_template('success.html')
    else :
        return render_template('fail.html')
    
@app.route('/')
def get():
   return render_template('login.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 