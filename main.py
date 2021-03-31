from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['username'] != 'Tester' or request.form['password'] != 'test':
            return redirect(url_for('home'))
        else:
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

@app.route('/register')
def register():
    return render_template('createUser.html')

@app.route('/forgotPassword')
def forgotPassword():
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run()