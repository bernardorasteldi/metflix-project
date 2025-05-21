# Metflix

**Metflix** é um sistema de biblioteca de filmes, séries e jogos inspirado na experiência de streaming da Netflix.

---

## 👥 Alunos/Desenvolvedores

- Bárbara Ferreira Rodrigues
- Bernardo Rasteldi Angelo
- Otávio Henrique Gonçalves Ribeiro

---

## 🛠️ Pré-requisitos

- Python 3.x
- virtualenv

---

## 🚀 Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/bernardorasteldi/metflix-project.git
   cd metflix
   ```

2. **Crie e ative um ambiente virtual**

   - **Navegue até a pasta metflix**

     ```bash
      É importante que o ambiente virtual seja configurado na pasta que contém o manage.py. Assim, caso ainda não esteja na pasta metflix, navegue até ela a partir da raiz.

      cd metflix
     ```

   - **Linux / macOS**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (CMD)**
     ```cmd
     python3 -m venv venv
     venv\Scripts\activate
     ```

3. **Instale as dependências**

   ```bash
   pip install django django-grappelli
   ```

---

## ▶️ Como executar

1. **Rodar o servidor de desenvolvimento**
   ```bash
   python3 manage.py runserver
   ```
   - Por padrão, o servidor ficará disponível em:
     ```text
     http://127.0.0.1:8000/
     ```

---

## 🔐 Superusuário (Admin)

- **Usuário:** `admin`
- **Senha:** `admin`

---

## 📖 Documentação

- Consulte a [documentação oficial do Django](https://docs.djangoproject.com/) para mais detalhes.

---

**Obrigado!** 🎬🚀
