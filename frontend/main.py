from flask import Flask, render_template
from EquityBulls import limited

app = Flask(__name__) #define app

@app.route('/') #path set
def home():
    return render_template('index.html')

@app.route('/news') #path set
def news():
    return render_template('news.html',limited=limited)

app.run(debug=True)
