from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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

@app.route('/register')
def register():
    return render_template('createUser.html')

@app.route('/forgotPassword')
def forgotPassword():
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run()