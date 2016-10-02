from flask import Flask, render_template


#init
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return render_template('app.html')

@app.route('/app/<seq>')
def seq(seq):
    return render_template(seq+'.html')


if __name__ == '__main__' :
    app.run()
