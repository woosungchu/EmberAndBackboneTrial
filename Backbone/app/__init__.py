from flask import Flask, render_template
import os

#init
app = Flask(__name__)

#Global Variables
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT,'static/')

app.debug = True

@app.route('/')
def hello():
    return render_template('app.html')

@app.route('/app/<seq>')
def seq(seq):
    return render_template(seq+'.html')

@app.route('/users')
def users():
    return '{"users": [{"id": 1,"screen_name": "steveWINton","messages": [1, 2, 3]}]}'

@app.route('/messages')
def messages():
    return '{"messages": [{"id": 1,"text": "Hello lovely world","user_id": 1}, {"id": 2,"text": "Hello again","user_id": 1}, {"id": 3,"text": "Goodbye, cruel world :(","user_id": 1}]}' 

if __name__ == '__main__' :
    app.run()
