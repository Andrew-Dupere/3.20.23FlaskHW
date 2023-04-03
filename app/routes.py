from app import app
from flask import render_template

@app.route('/')
def hello_world():

    listofthings = ['Sushi','Steak','Ice Cream','Fruit','Cheese']

    return render_template('index.html', listofthings = listofthings)


@app.route('/page2')
def pagetwo():
    listofthings = ['Sushi','Steak','Ice Cream','Fruit','Cheese']
    
    return render_template('page2.html', things = listofthings, name = 'Andrew')

