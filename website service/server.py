from flask import Flask
app = Flask(__name__)

@app.route('/add')
def add():
    return str(10 + 20)

app.run(port=5000)
