from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        last_login DATETIME,
        login_count INTEGER
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    now = datetime.now()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    if user:
        cursor.execute('''
        UPDATE users
        SET last_login = ?, login_count = login_count + 1
        WHERE email = ?
        ''', (now, email))
    else:
        cursor.execute('''
        INSERT INTO users (email, last_login, login_count)
        VALUES (?, ?, 1)
        ''', (email, now))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'email': email})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
