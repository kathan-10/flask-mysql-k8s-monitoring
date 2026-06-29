from flask import Flask, render_template, request, redirect, session
import mysql.connector
import time

app = Flask(__name__)

app.secret_key = "secretkey"

connected = False

while not connected:
    try:
        db = mysql.connector.connect(
            host="mysql-service",
            user="root",
            password="root",
            database="todo_db"
        )

        connected = True

    except:
        print("Waiting for MySQL...")
        time.sleep(5)

cursor = db.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
)
""")

# Tasks Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255),
    user_id INT
)
""")

db.commit()


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )

        db.commit()

        return redirect('/login')

    return render_template('register.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()

        if user:

            session['user_id'] = user[0]
            session['username'] = user[1]

            return redirect('/')

        return "Invalid Username or Password"

    return render_template('login.html')


# Home
@app.route('/')
def index():

    if 'user_id' not in session:
        return redirect('/login')

    cursor.execute(
        "SELECT * FROM tasks WHERE user_id=%s",
        (session['user_id'],)
    )

    tasks = cursor.fetchall()

    return render_template(
        'index.html',
        tasks=tasks,
        username=session['username']
    )


# Add Task
@app.route('/add', methods=['POST'])
def add():

    if 'user_id' not in session:
        return redirect('/login')

    task = request.form['task']

    cursor.execute(
        "INSERT INTO tasks (task, user_id) VALUES (%s, %s)",
        (task, session['user_id'])
    )

    db.commit()

    return redirect('/')


# Delete Task
@app.route('/delete/<int:id>')
def delete(id):

    if 'user_id' not in session:
        return redirect('/login')

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')


# Logout
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
