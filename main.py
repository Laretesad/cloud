from flask import Flask, render_template, request
from srv import sing
from srv2 import sing2

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=="POST":
        filename=request.form['name']
        ret=sing(filename)
        if ret==-1:
            ret=sing2(filename)
        print(ret)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
