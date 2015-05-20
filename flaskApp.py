from flask import Flask, render_template
from services import googleGrabber 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/scrape/')
@app.route('/scrape/<query>')
def scrape(query="nbc"):
    results = []
    results = googleGrabber.scrape_from_query(query)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.debug = True
    app.run()
