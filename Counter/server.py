from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/', methods=['GET'])
def index():
    if session['sessionCtr'] > 0:
        session['sessionCtr'] += 1
    else:
        session['sessionCtr'] = 1

    return render_template("counter.html")

@app.route('/ninja', methods=['POST'])
def ninja():

    session['sessionCtr'] += 1  # Only add 1 more as the normal page reload will also inc the page counter

    return redirect('/')

@app.route('/hacker', methods=['POST'])
def hacker():

    session['sessionCtr'] = 0  # Reset to 0

    return redirect('/')


app.run(debug=True)
