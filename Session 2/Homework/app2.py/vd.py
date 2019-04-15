from flask import Flask , render_template
app = Flask(__name__)

@app.route('/<int:a>/<int:b>')
def tinh(a,b) :
    return str(a+b)

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port = 5000, debug=True)
   