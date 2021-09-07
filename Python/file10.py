from flask import Flask



app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome and  hello to my world"


if __name__ == '__main__':

    app.run()

