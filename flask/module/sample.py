from flask import Flask
from urllib.parse import urlparse
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World!!"
    return name

@app.route('/sql')
def sql():
    url = urlparse('mysql://sample:sample@db:3306/sample')

    conn = mysql.connector.connect(
        host = url.hostname,
        port = url.port,
        user = url.username,
        password = url.password,
        database = url.path[1:],
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_table')
    rows = cur.fetchall()
    for row in rows:
        result = row

    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)