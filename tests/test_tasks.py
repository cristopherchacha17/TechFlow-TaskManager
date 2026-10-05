import pytest
import sqlite3
import os

# Caminho para o banco de dados de testes
DB_PATH = os.path.join(os.path.dirname(__file__), '../src/tasks.db')

@pytest.fixture
def setup_db():
    """Garante que a tabela exista antes dos testes."""
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
    yield
    # Limpa a tabela após os testes para não acumular lixo
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE title LIKE 'Teste %'")
    conn.commit()
    conn.close()

def test_criar_tarefa(setup_db):
    """Teste 1: Validar criação de uma tarefa no banco."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
        ("Teste Criar", "Descricao do teste", "A Fazer", "Alta")
    )
    conn.commit()
    
    cursor.execute("SELECT title, priority FROM tasks WHERE title = 'Teste Criar'")
    task = cursor.fetchone()
    conn.close()
    
    assert task is not None
    assert task[0] == "Teste Criar"
    assert task[1] == "Alta"

def test_editar_tarefa(setup_db):
    """Teste 2, 4 e 5: Validar edicao, alteracao de status e prioridade."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
        ("Teste Editar", "Antes", "A Fazer", "Baixa")
    )
    conn.commit()
    
    # Atualiza o status e a prioridade
    cursor.execute(
        "UPDATE tasks SET status = ?, priority = ? WHERE title = ?",
        ("Em andamento", "Média", "Teste Editar")
    )
    conn.commit()
    
    cursor.execute("SELECT status, priority FROM tasks WHERE title = 'Teste Editar'")
    task = cursor.fetchone()
    conn.close()
    
    assert task[0] == "Em andamento"
    assert task[1] == "Média"

def test_excluir_tarefa(setup_db):
    """Teste 3: Validar a exclusao de uma tarefa."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)",
        ("Teste Excluir", "Vai sumir", "A Fazer", "Baixa")
    )
    conn.commit()
    
    # Exclui o registro
    cursor.execute("DELETE FROM tasks WHERE title = 'Teste Excluir'")
    conn.commit()
    
    cursor.execute("SELECT * FROM tasks WHERE title = 'Teste Excluir'")
    task = cursor.fetchone()
    conn.close()
    
    assert task is None
