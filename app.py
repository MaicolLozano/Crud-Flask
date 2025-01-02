from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="",    
    database="employes",
    port="3307"
)

def get_employes():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employes")
    employes = cursor.fetchall()
    cursor.close()
    return employes

@app.route('/')
def index():
    return render_template('index.html', employes=get_employes())

@app.route('/actualizar/<int:employe_id>', methods=['GET'])
def actualizar(employe_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employes WHERE id = %s", (employe_id,))
    employe = cursor.fetchone()
    cursor.close()
    return render_template('actualizar.html', employe=employe)

@app.route('/update/<int:employe_id>', methods=['POST'])
def update(employe_id):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    cursor = mydb.cursor()
    cursor.execute("UPDATE employes SET name = %s, email = %s, phone = %s, address = %s WHERE id = %s", (name, email, phone, address, employe_id))
    mydb.commit()
    cursor.close()

    return redirect(url_for('index'))

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    cursor = mydb.cursor()
    cursor.execute("INSERT INTO employes (name, email, phone, address) VALUES (%s, %s, %s, %s)", (name, email, phone, address))
    mydb.commit()
    cursor.close()

    return redirect(url_for('index'))


@app.route('/delete/<int:employe_id>', methods=['POST'])
def delete(employe_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM employes WHERE id = %s", (employe_id,))
    mydb.commit()
    cursor.close()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)