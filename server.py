# jsonify lets us send JSON back!
from flask import Flask, render_template, request, redirect, jsonify
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'notes')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/notes/create', methods=['POST'])
def create():
    query = "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())"
    data = {
        'title': request.form['title']
    }
    mysql.query_db(query, data)
    return redirect('/notes')

@app.route('/notes/<id>/delete')
def delete(id):
    query = "DELETE FROM notes WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/notes')

@app.route('/notes/<id>/update', methods=['POST'])
def update(id):
    query = "UPDATE notes SET description = :desc WHERE id = :id"
    data = {
        'id': id,
        'desc': request.form['description']
    }
    mysql.query_db(query, data)
    return redirect('/notes')

@app.route('/notes')
def notes():
    show_notes = mysql.query_db("SELECT * FROM notes")

    return render_template('notes.html', notes = show_notes)


app.run(debug=True)
