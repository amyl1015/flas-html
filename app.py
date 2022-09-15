from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Amy.html')

@app.route('/1')
def Section():
    return render_template('Amy2.html')

@app.route('/2')
def bootstrap():
    return render_template('AmyBootstrap.html')

@app.route('/3')
def bootstrap2():
    return render_template('AmyBootstrap2.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)

 