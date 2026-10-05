from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__, template_folder='../templates')

# Caminho absoluto para encontrar o banco de dados correto
DB_PATH = os.path.join(os.path.dirname(__file__), 'tasks.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route("/")
def home():
    # R - Read: Listagem de tarefas (Issue 4)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, status, priority FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    # C - Create: Cadastro de tarefas (Issue 3)
    title = request.form.get("title")
    description = request.form.get("description")
    priority = request.form.get("priority")
    status = "A Fazer"  # Toda tarefa nova começa como 'A Fazer'

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
        (title, description, status, priority)
    )
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
