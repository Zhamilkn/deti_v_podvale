from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from data import data
import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/deti')
def deti():
    return render_template("deti.html", data=data)

@app.route('/add_card', methods=['POST'])
def add_card():
    card = {}
    card['id'] = datetime.datetime.now()
    card['child_name'] = request.form ['child_name']
    card['child_lastname'] = request.form ['child_lastname']
    card['child_height'] =  request.form ['child_height']
    card['child_weight'] = request.form ['child_weight']
    card['child_foot_size'] = request.form ['child_foot_size']
    card['age'] = request.form ['age']
    data.append(card)
    print(card)
    return redirect('/')

@app.route('/delete_card', methods=['POST'])
def delete_card():
    id = request.form["id"]
    for card in data:
        print(str(id))
        if str(card['id']) == str(id):
            data.remove(card)
        return redirect('/deti')


if __name__ == '__main__':
    app.debug = True
    app.run()

