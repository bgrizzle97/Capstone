from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import dataset

import passwords

app = Flask(__name__)
db = dataset.connect('sqlite:///user.db')

userID = 1

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        profile = db['user'].find_one(username=username)
        if profile == None:
            return redirect(url_for('home'))
            return
        if (not passwords.verify_password(password, profile["password"])):
            return redirect(url_for('home'))
            return
        
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
        db['user'].insert({'id':userID, 'username':username, 'email':email, 'password':password})
        return redirect(url_for('home'))
    return render_template('createUser.html')

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        username = request.form['username']
        password = passwords.encode_password(request.form['password'])
        profile = db['user'].find_one(username=username)
        if profile == None:
            return redirect(url_for('forgotPassword'))
            return
        db['user'].update({'username':username, 'password':password},['username'])
        return redirect(url_for('home'))
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run()