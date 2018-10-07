from flask import Flask
app = Flask(__name__)
import subprocess

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
    seg = 1
    subprocess.call("shutdown -s 1")