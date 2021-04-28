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

userID = random.randint(0000000000000, 9999999999999)

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
        password = request.form['password']
        password2 = request.form['password2']
        passwordSafe = passwords.encode_password(password)
        global userID
        profile = db['user'].find_one(id=userID)
        while profile != None:
            userID = random.randint(0000000000000, 9999999999999)
            profile = db['user'].find_one(id=userID)
        if password == password2:
            db['user'].insert({'id':userID, 'username':username, 'email':email, 'password':passwordSafe, 'verified':0})
            db.commit()
        else:
            return redirect(url_for('register'))
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
    global otp
    global otpp 
    if otp == int(user_otp):  
        db['user'].update({'username':username, 'verified':1},['username'])
        db.commit()
        otp = random.randint(000000000, 999999999)
        return redirect(url_for('home'))
    elif otpp == int(user_otp):
        db['user'].update({'username':username, 'verified':1},['username'])
        db.commit()
        otpp = random.randint(000000000, 999999999)
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
            msg = Message('OTP',sender = 'nflstatking@gmail.com', recipients = [profile['email']])  
            msg.body = "We noticed some suspicious behavior on your account as someone has tried to access it. \n \n We recommend changing your password in order to keep your account secure."  
            mail.send(msg)
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

@app.route('/SF')
def SF():
    return render_template('SF.html')

@app.route('/CHI')
def CHI():
    return render_template('CHI.html')

@app.route('/CIN')
def CIN():
    return render_template('CIN.html')

@app.route('/DEN')
def DEN():
    return render_template('DEN.html')

@app.route('/BUF')
def BUF():
    return render_template('BUF.html')

@app.route('/CLE')
def CLE():
    return render_template('CLE.html')

@app.route('/TB')
def TB():
    return render_template('TB.html')

@app.route('/ARI')
def ARI():
    return render_template('ARI.html')

@app.route('/LAC')
def LAC():
    return render_template('LAC.html')

@app.route('/KC')
def KC():
    return render_template('KC.html')

@app.route('/IND')
def IND():
    return render_template('IND.html')

@app.route('/DAL')
def DAL():
    return render_template('DAL.html')

@app.route('/MIA')
def MIA():
    return render_template('MIA.html')

@app.route('/PHI')
def PHI():
    return render_template('PHI.html')

@app.route('/ATL')
def ATL():
    return render_template('ATL.html')

@app.route('/NYG')
def NYG():
    return render_template('NYG.html')

@app.route('/JAX')
def JAX():
    return render_template('JAX.html')

@app.route('/NYJ')
def NYJ():
    return render_template('NYJ.html')

@app.route('/DET')
def DET():
    return render_template('DET.html')

@app.route('/GB')
def GB():
    return render_template('GB.html')

@app.route('/CAR')
def CAR():
    return render_template('CAR.html')

@app.route('/NE')
def NE():
    return render_template('NE.html')

@app.route('/LV')
def LV():
    return render_template('LV.html')

@app.route('/HOU')
def HOU():
    return render_template('HOU.html')

@app.route('/TEN')
def TEN():
    return render_template('TEN.html')

@app.route('/BAL')
def BAL():
    return render_template('BAL.html')

@app.route('/MIN')
def MIN():
    return render_template('MIN.html')

@app.route('/SEA')
def SEA():
    return render_template('SEA.html')

@app.route('/LA')
def LA():
    return render_template('LA.html')

@app.route('/NO')
def NO():
    return render_template('NO.html')

@app.route('/WAS')
def WAS():
    return render_template('WAS.html')


if __name__ == '__main__':
    app.run()