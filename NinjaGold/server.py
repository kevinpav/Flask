from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

## Define RandomNum function here
def getRandomGold(minNum, maxNum):
    return random.randrange(minNum,maxNum+1)
##

@app.route('/', methods=['GET'])
def index():
    # session['myGold'] = 0
    # session['myActivity'] = ''

    return render_template("index.html")
##

@app.route('/process_money', methods=['POST'])
def process_money():
    print request.form
    if request.form['building'] == 'farm':
        # 10-20 gold
        minedGold = getRandomGold(10,20)
    elif request.form['building'] == 'cave':
        # 5-10 gold
        minedGold = getRandomGold(5,10)
    elif request.form['building'] == 'house':
        # 2-5 gold
        minedGold = getRandomGold(2,5)
    elif request.form['building'] == 'casino':
        # -50 to + 50 gold
        minedGold = getRandomGold(-50,50)
    elif request.form['building'] == 'reset':
        # Reset mining operations
        session['myGold'] = 0
        session['myActivity'] = ""
        return redirect('/')
    else:
        print "Nothing to do!"
        minedGold = 0

    try:
        session['myGold'] += minedGold  # Check if variable is defined
    except KeyError:
        session['myGold'] = 0  # If not, initialize both
        session['myActivity'] = ''

    actLog = "Mined " + str(minedGold) + " gold from the " + request.form['building'] + "!\r\n"

    if ((minedGold < 0) and (session['myGold'] < 0)):
        actLog += "  OH NOES!!!\r\n"

    session['myActivity'] += actLog

    return redirect('/')
##

@app.route('/playagain', methods=['POST'])
def hacker():
    session['randomNum'] = 0  # Reset to 0
    session['lastGuess'] = ''
    return redirect('/')
##

app.run(debug=True)
