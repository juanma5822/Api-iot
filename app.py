from flask import Flask, redirect, url_for, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)   
app.config['MYSQL_HOST'] = 'ec2-34-227-120-79.compute-1.amazonaws.com'
app.config['MYSQL_USER'] = 'xxbafeigeplqzf'
app.config['MYSQL_PASSWORD'] = '292103424cc1246aebe3a724ba93b366f7bcb06ae9d2c700b1cfd305b03e6d80'
app.config['MYSQL_DB'] = 'd4reu6rdlo91uc'
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
    app.run(port=5432)

