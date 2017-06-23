from flask import Flask, render_template, request, redirect, session, flash
# Import the RegEx module
import re
# Create the regex we will use to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.]')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    print request.form
    myName = request.form['name'].strip()
    myLocation = request.form['location'].strip()
    myLanguage = request.form['language'].strip()
    myComments = request.form['comments'].strip()
    myEmail = request.form['email'].strip()
    if len(myName) < 1:
        flash("Name cannot be empty!")
    elif len(myComments) < 1:
        flash("Comment cannot be empty!")
    elif len(myComments) > 120:
        flash("Please keep comments less than 120 letters!")
    elif len(myEmail) < 1:
        flash("Email cannot be empty!")
    elif not EMAIL_REGEX.match(myEmail):
        flash("Invalid Email!")
    else:
        flash("Success!")
        return render_template("result.html", name=myName, email=myEmail, location=myLocation, language=myLanguage, comments=myComments)

    return redirect('/')

app.run(debug=True)
