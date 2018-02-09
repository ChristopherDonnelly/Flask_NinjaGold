'''
You'll be rewriting your Disappearing Ninja assignment to include AJAX. The below steps will help you get started. Next, follow the wireframe below to build a version of Disappearing Ninja with AJAX. Remember, with AJAX, you will only need one view and your page should never be reloaded.

1. Create a new Flask project. Build it with one get route to serve up your index.html. Test to make sure you can run that server and load the html page before continuing.

2. Create a static directory with your JavaScript file inside of it. Now link your JS file to your index.html file. Test it by asking for an alert box on page load. Don't forget to link to the jQuery CDN, too. You'll be using it for AJAX just like before.

3. You'll need some event listeners in order to trigger a request to the server when a user clicks one of the color buttons.

4. When an event occurs (button click), you'll want to send a request to the server. The server should collect information about which Ninja you'd like to display, along with the correct message, and send a JSON response to the client.
'''

# Import Flask to allow us to create our app, and import
# render_template to allow us to render HTML Files.
from flask import Flask, render_template, request, redirect, jsonify, session
import random
import json
import datetime
import time

app = Flask(__name__)

app.secret_key = 'NinjaGoldSecretKey'

@app.route('/')

def display_index():
    if not 'gold' in session:
        session['gold'] = 0

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])         

def process_money():

    data = json.loads(request.data)

    building = data.split("=")[1]

    msg = ""
    time = datetime.datetime.now().strftime('%I:%M:%S%p %m/%d/%Y')

    if building == 'farm':
        gold = random.randrange(10, 21)
        msg = 'Earned {} Gold from helping the farmer! {}'.format(gold, time)
    elif building == 'cave':
        gold = random.randrange(5, 11)
        msg = 'Earned {} Gold while exploring the cave! {}'.format(gold, time)
    elif building == 'house':
        gold = random.randrange(2, 6)
        msg = 'Earned {} Gold while crafting in the house! {}'.format(gold, time)
    elif building == 'casino':
        gold = random.randrange(0, 51)
        chance = random.randrange(0, 2)
        earnedLost = 'Earned'
        cheer = 'Hooray.'
        if chance == 1:
            gold *= -1
            earnedLost = 'Lost'
            cheer = 'Ouch.'

        msg = '{} {} Gold gambling in the Casino!... {} {}'.format(earnedLost, gold, cheer, time)

    session['gold'] += gold
    
    return jsonify(message=msg,gold=session['gold'])

app.run(debug=True)