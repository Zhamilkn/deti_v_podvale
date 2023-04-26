from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from data import data
import datetime
import os


app = Flask(__name__)

def write_data(data):
    with open('data.py', 'w', encoding="utf-8") as f:
        f.write(data)

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/deti')
def deti():
    return render_template("deti.html", data=data)


@app.route('/add_card', methods=['POST'])
def add_card():
    card = {}
    card ['id'] = str(datetime.datetime.now())[-6:-1]
    card ["child_name"] = request.form["child_name"]
    card ['child_lastname'] = request.form ['child_lastname']
    card ['child_height'] =  request.form ['child_height']
    card ['child_weight'] = request.form ['child_weight']
    card ['child_foot_size'] = request.form ['child_foot_size']
    card ['height'] = request.form ['height']
    card ["overall_rating"] = request.form ["overall_rating"]
    card ['age'] = request.form ['age']
    image = request.files["image"]
    filename = f"{card['id']}.jpg"
    file_path = os.path.join('static,' 'cards', filename).replace("\\","/")
    image.save(file_path)

    data.append(card)
    write_data(f"data = {data}")
    return redirect('/admin')


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


