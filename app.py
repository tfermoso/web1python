from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route('/login',methods=['GET'])
def index():
    return render_template("index.html")

#recibir dos parametros nombre y edad
@app.route('/saludo/<nombre>/<int:edad>')
def prueba(nombre,edad):
    if(edad<18):
        return "Hola "+nombre+" eres menor de edad"
    else:
        return "Hola "+nombre+" eres mayor de edad"

#login post
@app.route('/login',methods=['POST'])
def login():
    #obtener los datos del formulario
    username = request.form['username'] 
    password = request.form['password']
    if(username == 'admin' and password == 'admin'):
        #guardar datos en session
        session['username'] = username
        return redirect(url_for('admin'))

    else:
         return render_template("index.html",mensaje="Usuario o contraseña incorrecta")

    
    
@app.route('/admin',methods=['GET'])
def admin():
    if(session["username"]):
        return render_template("admin/admin.html")
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':    
    app.run(debug=True,port=80)
    