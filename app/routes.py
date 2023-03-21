from app import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/page2')
def pagetwo():

    
    return render_template('page2.html')

