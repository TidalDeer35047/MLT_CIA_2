from flask import Flask, render_template, request, redirect
import vader
import pymysql as pm

my_db = pm.connect(user = "root" , host = "localhost" , password = "passc123" , database = "ML")
cur = my_db.cursor()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    passw = request.form['password']
    cur.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = "+username+";")
    data = cur.fetchall()
    if (data[0] == passw):
        render_template("home.html")
    else:
        redirect("/")
    #return render_template("home.html")

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    negative, neutral, positive, compound, overall_sentiment = vader.sentiment_vader(prompt)
    output = "The sentiment scores of the  prompt are as follows:\nNegative: " + str(negative) + "\nNeutral: " + str(neutral) + "\nPositive: " + str(positive) + "\nCompound: " + str(compound) + "." + "\nThe overall sentiment is: " + str(overall_sentiment) + "."

    return render_template('home.html', output=output)



if __name__ == '__main__':
    app.run(debug=True)
