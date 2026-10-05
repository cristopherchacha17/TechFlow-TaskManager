from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__, template_folder='../templates')

DB_PATH = os.path.join(os.path.dirname(__file__), 'tasks.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    # Adicionamos essa linha abaixo para conseguirmos acessar os dados pelo nome da coluna no HTML (ex: task['id'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, status, priority FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    description = request.form.get("description")
    priority = request.form.get("priority")
    status = "A Fazer"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
        (title, description, status, priority)
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update_task(id):
    status = request.form.get("status")
    priority = request.form.get("priority")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET status = ?, priority = ? WHERE id = ?",
        (status, priority, id)
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
