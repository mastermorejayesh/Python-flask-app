from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database configuration
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

@app.route('/')
def index():
    connection = None
    cursor = None
    users = []
    usersheader = []
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Fetch users data
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()

        # Fetch usersheader data
        cursor.execute("SELECT header FROM usersheader")
        usersheader = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return render_template('index.html', users=users, usersheader=usersheader)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

        return redirect(url_for('index'))

    return render_template('add_user.html')

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return redirect(url_for('index'))

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    connection = None
    cursor = None

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

        return redirect(url_for('index'))

    user = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
