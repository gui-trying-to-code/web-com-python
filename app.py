from flask import Flask

app = Flask("my app")

@app.route('/')
def hello ():
    return "Hello, world!"