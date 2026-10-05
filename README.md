# TechFlow TaskManager 🚀

Sistema web completo para gerenciamento dinâmico de tarefas (CRUD) desenvolvido em Python com Flask e banco de dados SQLite. O projeto adota metodologias ágeis e práticas modernas de Engenharia de Software, incluindo testes automatizados e Integração Contínua (CI).

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python + Flask
* **Banco de Dados:** SQLite3
* **Testes:** Pytest
* **CI/CD:** GitHub Actions (Execução automatizada de testes a cada Push)
* **Metodologia:** Kanban (GitHub Projects)

## 📋 Funcionalidades (CRUD)
* **Create:** Cadastro de tarefas com título, descrição e níveis de prioridade (Baixa, Média, Alta).
* **Read:** Listagem dinâmica das tarefas salvas no banco.
* **Update:** Alteração inline de prioridade e status da atividade (A Fazer, Em andamento, Concluído).
* **Delete:** Exclusão definitiva de registros com confirmação em tela.

## 🧪 Estrutura de Testes Automatizados
O projeto conta com testes unitários para validar o comportamento do banco e das rotas:
```bash
# Para rodar os testes localmente:
pytest
```

## 📈 Integração Contínua
Configurado via GitHub Actions (`.github/workflows/tests.yml`) para validar a integridade do código em todas as submissões automaticamente.
