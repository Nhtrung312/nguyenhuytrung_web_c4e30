from flask import Flask , render_template , url_for,redirect
app = Flask(__name__)

@app.route('/about-me')
def aboutme() :
    me = {
        'name' : 'Nguyễn Huy Trung',
        'work' : 'sinh viên',
        'school' : 'hvtc',
        'hobbies' : 'music,coding,tech,sport'
    }
    
    return render_template('about.html',data=me)

@app.route('/school')
def truong():
    return redirect("http://techkids.vn")

if __name__ == '__main__' :
    app.run(host = '127.0.0.1', port=5000 , debug=True )