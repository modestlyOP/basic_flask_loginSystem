from secrets import token_hex
from flask import Flask, flash, render_template, redirect, request, url_for
from usr_mgmt import add_usr, chk_usr_exists, chk_login

app = Flask(__name__)
app.secret_key = b'{token_hex()}'

@app.route('/')
def indx():
    return render_template('index.html')

@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    saveState = 0           #tells html page what to display when form is submitted

    if request.method == 'POST':
        result = request.form
        fname = result.get('fname')
        lname = result.get('lname')
        username = result.get('username')
        password = result.get('password')
        email = result.get('email')
        if fname and lname and username and password and email:
            if chk_usr_exists(username) is None:
                add_usr(fname, lname, username, password, email)
                saveState = 1
                flash("User registration successful")
                print("User registration successful")           #debug print
            else:
                saveState = 2
                flash("Username taken!")
                print("Username taken!")           #debug print
                
    return render_template('auth/registration.html', saveState=saveState)

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    login_success = 0
    if request.method == 'POST':
        result = request.form
        username = result.get('username')
        password = result.get('password')
        if username and password:
            if chk_usr_exists(username) == (1,):
                if chk_login(username, password):
                    flash("Login successful")
                    print("Login successful")
                    login_success = 1
                    return redirect(url_for('acc'))
                else:
                    flash("Login denied")
                    print("Login denied")
                    login_success = 2

    return render_template('auth/signin.html', login_success=login_success)

@app.route('/acc/')
def acc():
    return "<h1>PAGE UNDER CONSTRUCTION</h1>"