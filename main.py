from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.environ['DB_HOST'],
                            database=os.environ['DB_NAME'],
                            user=os.environ['DB_USER'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app. Edited at 26th Dec 3:00 PM."})

@app.route('/db')
def db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
