from flask import Flask
from urllib.parse import urlparse
import mysql.connector
#from sqlalchemy import *
#from sqlalchemy.orm import *
#from sqlalchemy.ext.declarative import declarative_base

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
    result = cur.fetchall()

    '''
    DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
        "sample",
        "sample",
        "db",
        "sample",
    )
    ENGINE = create_engine(
        DATABASE,
        encoding = "utf-8",
        echo=True
    )
    session = scoped_session(
        sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = ENGINE
        )
    )

    t = text("SELECT * FROM test_table LIMIT 1")
    result = db.session.execute(t)
    '''

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)