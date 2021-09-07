
from flask import Flask
from flask_mail import Mail

app = Flask('gmail')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'prince93101@gmail.com'
app.config['MAIL_PASSWORD'] = 'Prince@99'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
  msg = Message('Hello from the other side!', sender =   'prince93101@gmail.com', recipients = ['pwenceprince99@gmail.com'])
  msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
  mail.send(msg)
  return "Message sent!"

if __name__ == '__main__':
   app.run(debug = True)
   
   
from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html",content="Testing")
if __name__ == '__main__':
   app.run()
