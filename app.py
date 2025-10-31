from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route('/')
def welcome_page():
    return "Welcome to the home page"
    

@app.route('/count')
def visitNu():
    counter = r.incr('counter')
    return f"<h1>Number of count is: {counter} </h1>"


if __name__ == '__main__':
    app.run("0.0.0.0", 5001)
