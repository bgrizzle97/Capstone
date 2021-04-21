from flask import Flask, render_template, request, redirect, url_for, g, flash
from flask_mail import *
import sqlite3
import dataset
import random

import passwords

app = Flask(__name__)
mail = Mail(app)
db = dataset.connect('sqlite:///user.db')

app.config["SECRET_KEY"] = 'f1/2f1uf98jongin3f13/f1f31hf912nf/vdshfanvpirbeoj'

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'nflstatking@gmail.com'  
app.config['MAIL_PASSWORD'] = 'statistic'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  

mail = Mail(app)
otp = random.randint(000000000, 999999999)
otpp = random.randint(000000000, 999999999)

userID = 1

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        profile = db['user'].find_one(username=username)
        if profile == None:
            return redirect(url_for('home'))
        if (not passwords.verify_password(password, profile["password"])):
            return redirect(url_for('home'))
        if profile['verified'] == 0:
            return redirect(url_for('register'))
        
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/teamComparison')
def teamComparison():
    return render_template('teamComparison.html')

@app.route('/teamPage')
def teamPage():
    return render_template('teamPage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = passwords.encode_password(request.form['password'])
        global userID
        profile = db['user'].find_one(id=userID)
        while profile != None:
            userID += 1
            profile = db['user'].find_one(id=userID)
        db['user'].insert({'id':userID, 'username':username, 'email':email, 'password':password, 'verified':0})
        db.commit()
        msg = Message('OTP',sender = 'nflstatking@gmail.com', recipients = [email])  
        msg.body = "Here is your one time passcode for verifying your NFL Stat King Account: \n" + str(otp)  
        mail.send(msg) 
        return redirect(url_for('verify'))
    return render_template('createUser.html')

@app.route('/verify', methods = ["GET", "POST"])  
def verify(): 
    return render_template('verify.html')

@app.route('/validate', methods=["GET", "POST"])
def validate():
    user_otp = request.form['otp']
    username = request.form['username']  
    if otp == int(user_otp):  
        db['user'].update({'username':username, 'verified':1},['username'])
        db.commit()
        return redirect(url_for('home'))
    elif otpp == int(user_otp):
        db['user'].update({'username':username, 'verified':1},['username'])
        db.commit()
        return redirect(url_for('home'))
    return "<h3>Failure, OTP does not match</h3>"  

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = passwords.encode_password(request.form['password'])
        profile = db['user'].find_one(username=username)
        db['user'].update({'username':username, 'verified':0},['username'])
        if profile == None:
            return redirect(url_for('forgotPassword'))
        if profile['email'] != email:
            flash('Incorrect email entered')
            return redirect(url_for('forgotPassword'))
        db['user'].update({'username':username, 'password':password},['username'])
        db.commit()
        msg = Message('OTP',sender = 'nflstatking@gmail.com', recipients = [email])  
        msg.body = "Here is your one time passcode for changing your password: \n" + str(otpp)  
        mail.send(msg) 
        return redirect(url_for('verify'))
    return render_template('forgot_password.html')

@app.route('/PIT')
def PIT():
    return render_template('PIT.html')

if __name__ == '__main__':
    app.run()