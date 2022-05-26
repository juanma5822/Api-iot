from flask import Flask, redirect, url_for, request, json
import psycopg2
app = Flask(__name__)   
conexion=psycopg2.connect(user='xxbafeigeplqzf',
                          password='292103424cc1246aebe3a724ba93b366f7bcb06ae9d2c700b1cfd305b03e6d80',
                          host='ec2-34-227-120-79.compute-1.amazonaws.com',
                          port=5432,
                          database='d4reu6rdlo91uc')

cursor=conexion.cursor()

@app.route("/")
def Home():
    return 'desplegado'


@app.route("/getData")
def index():
    cursor
    sql=("SELECT * FROM datosrecibidos ")
    cursor.execute(sql)
    data = cursor.fetchall()
    response = data
    return(json.dumps(response))

if __name__ == '__main__':
    app.run(port=5432)

