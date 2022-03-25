import imp
from flask import Flask, render_template
from EquityBulls import limited
from iifl import limitedIifl

app = Flask(__name__) #define app

@app.route('/') #path set
def home():
    return render_template('index.html')

@app.route('/equitybulls') #path set
def EQ():
    return render_template('newsEquity.html',limited=limited)

@app.route('/iifl') #path set
def iifl():
    return render_template('newsIifl.html',limitedIifl=limitedIifl)

app.run(debug=True)
