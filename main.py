from flask import Flask, redirect, url_for, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'ec2-34-227-120-79.compute-1.amazonaws.com'
app.config['MYSQL_USER'] = 'mlsrxudbzbqxlx'
app.config['MYSQL_PASSWORD'] = 'b25c9ec282a5af40a9a1b1b790616a8c94b6c446fce3a0f5604225251c2cd621'
app.config['MYSQL_DB'] = 'd9s8mci0uikpqd'
app.config['MYSQL_PORT']= 5432
mysql = MySQL(app)

@app.route("/getData")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM database")
    data = cur.fetchall()
    cur.close()
    return(data)

if __name__ == '__main__':
    app.run(port=5000)

