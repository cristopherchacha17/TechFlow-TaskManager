import sqlite3
import os

# Define o caminho do banco de dados para ficar dentro da pasta src
DB_PATH = os.path.join(os.path.dirname(__file__), 'tasks.db')

def init_db():
    """Cria a tabela de tarefas caso ela não exista."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso! ✅")

if __name__ == "__main__":
    init_db()
