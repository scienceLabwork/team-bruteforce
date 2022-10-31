from flask import Flask, render_template, request, redirect
import time
import mysql.connector
import os
import sqlite3

app = Flask(__name__,static_url_path='', static_folder='frontend/static',template_folder='frontend/templates')
# port = int(os.environ.get("PORT", 5000))

#open sqlite database
con = sqlite3.connect('database.db',check_same_thread=False)
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name TEXT, email TEXT, message TEXT,stars TEXT, created_at TEXT)")
con.commit()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/review', methods=['POST', 'GET'])
def review():
    if(request.method == 'POST'):
        name = request.form.get('Nname')
        email = request.form.get('Nemail')
        message = request.form.get('Nmessage')
        print(name, email, message)
        cursor = con.cursor()
        cursor.execute("INSERT INTO users (name, email, message, created_at) VALUES ('{}', '{}', '{}', '{}')".format(str(name), str(email), str(message), time.strftime("%Y-%m-%d %H:%M:%S")))
        con.commit()
        return redirect('/submitForm')
    return render_template('review.html')

@app.route('/submitForm')
def Subform():
    return render_template('thankyou.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)