from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    print request.form
    myname = request.form['name']
    mylocation = request.form['location']
    mylanguage = request.form['language']
    mycomments = request.form['comments']
    return render_template("result.html", name=myname, location=mylocation, language=mylanguage, comments=mycomments)
    # return redirect('/')

app.run(debug=True)
