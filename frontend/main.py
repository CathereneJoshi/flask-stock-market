from flask import Flask, render_template
app = Flask(__name__) #define app

@app.route('/') #path set
def home():
    return render_template('index.html')

app.run(debug=True)
