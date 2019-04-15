from flask import Flask , render_template
app = Flask(__name__)
@app.route('/')
def index():
  poem = {
    'title' : 'tĩnh dạ tứ',
    'author' : 'lý bạch ',
    'body' : 'đầu hương '
  }
  return render_template('index.html',data=poem)

if __name__ == '__main__' :
  app.run(host='127.0.0.1' , port=8000 , debug=True)