import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(query, (username, password))
    result = cur.fetchone()
    return "Login Success" if result else "Login Failed"
