from flask import Flask , render_template 
app = Flask(__name__)

@app.route('/bmi/<float:weight>/<float:height>')
def ketqua(weight,height):
    
    BMI = float(weight)/((float(height)/100)**2)
    return render_template('bmi.html', bmi = BMI )

if __name__ == '__main__' :
    app.run(host = '127.0.0.1' , port = 8000 , debug = True)