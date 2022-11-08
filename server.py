from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'safe zone'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template("index.html", count=session['counter'])

@app.route('/addone')
def addone():
    session['counter'] += 0
    return redirect('/')
@app.route('/addtwo')
def addtwo():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')


app.run(debug=True)