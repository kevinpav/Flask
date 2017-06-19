from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

## Define RandomNum function here
def getRandomNum():
    return random.randrange(1,101)
##

@app.route('/', methods=['GET'])
def index():
    if session['randomNum'] < 1:
        session['randomNum'] = getRandomNum()
        session['lastGuess'] = ''

    return render_template("index.html")
##

@app.route('/guess', methods=['POST'])
def guess():

    session['lastGuess'] = request.form['lastguess']
    # print 'Your Guess:', session['myguess']
    # session['sessionCtr'] += 1  # Only add 1 more as the normal page reload will also inc the page counter

    return redirect('/')
##

@app.route('/playagain', methods=['POST'])
def hacker():
    session['randomNum'] = 0  # Reset to 0
    session['lastGuess'] = ''
    return redirect('/')
##

app.run(debug=True)
