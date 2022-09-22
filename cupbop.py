from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('galeria.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/SingUp')
def SingUp():
    return render_template('SingUp.html')

@app.route('/recoverAccount')
def recoverAcount():
    return render_template('recoverAccount.html')