from flask import Flask
import pymysql
import datetime

app = Flask(__name__)

DB_HOST = "kavya-db-1.cc8rwhxooogl.ap-southeast-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "AwsTiger123*"
DB_NAME = "flask_db"

@app.route('/log')
def log():
    connection = pymysql.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = connection.cursor()
    timestamp = datetime.datetime.now()
    cursor.execute("INSERT INTO logs (timestamp) VALUES (%s)", (timestamp,))
    connection.commit()
    connection.close()
    return "Logged at " + str(timestamp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
