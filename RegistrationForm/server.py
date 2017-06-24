from flask import Flask, render_template, request, redirect, session, flash
# Import the RegEx module
import re, datetime

# Create the regex we will use to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.]')
# Name validation - No numbers
NUMBER_REGEX = re.compile(r'\d')
# Password must contain 1 number and 1 UPPERCASE character.
PASSWORD_FORMAT = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
CRLF = "\r\n"
now = datetime.datetime.now()
app = Flask(__name__)
app.secret_key = 'MySuperSecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    print request.form
    formError = False
    # Put the form fields into local variables, stripping whitespace
    myFirstname = request.form['firstname'].strip()
    myLastname = request.form['lastname'].strip()
    myEmail = request.form['email'].strip()
    myPassword = request.form['password'].strip()
    myPassword2 = request.form['password2'].strip()
    myBirthdate = request.form['birthdate']
    # Test for invalid entries
    if len(myFirstname) < 1 or len(myLastname) < 1:
        flash("Name fields cannot be empty!")
        formError = True
    elif NUMBER_REGEX.search(myFirstname + myLastname):
        flash("Name fields cannot contain numbers!")
        formError = True
    # Test email
    if len(myEmail) < 1:
        flash("Email cannot be empty!")
        formError = True
    elif not EMAIL_REGEX.match(myEmail):
        flash("Invalid Email!")
        formError = True
    # Test Birthdate We will assume the date is valid because it is chosen from the "date" input type
    if datetime.datetime.strptime(myBirthdate, "%Y-%m-%d") > now:
        flash("Sorry birthdate cannot be in the future!")
        formError = True
    # Test passwords
    if len(myPassword) < 1:
        flash("Password cannot be empty!")
        formError = True
    elif len(myPassword) > 8:
        flash("Password cannot be longer than 8 characters!")
        formError = True
    elif len(myPassword2) < 1 or myPassword2 != myPassword:
        flash("Passwords do not match!")
        formError = True
    elif not PASSWORD_FORMAT.search(myPassword):
        flash("Password must contain 1 UPPERCASE and 1 NUMBER!")
        formError = True

    if formError != True:
        flash("Success!")
        return (render_template("result.html",
                    firstname=myFirstname,
                    lastname=myLastname,
                    email=myEmail,
                    birthdate=myBirthdate,
                    password=myPassword,
                    password2=myPassword2)
                )

    return redirect('/')

app.run(debug=True)
