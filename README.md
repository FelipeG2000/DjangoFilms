# 🎬 DjangoFilmStream

A RESTful Django project for managing and streaming films. Built with Django 5.2 and Django REST Framework.

---

## 📁 Project Structure
```
DjangoFilms/ │ 
├── .venv/ # Virtual environment (excluded from Git) 
├── DjangoFilmStream/ # Django project directory 
│ ├── DjangoFilmStream/ # Project settings, URLs, WSGI/ASGI 
│ ├── api/ # Main app for API logic 
│ ├── manage.py 
│ ├── .env # Environment variables 
│ └── requirements.txt # Project dependencies 
├── .gitignore 
└── README.md # You are here 📄
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-user/DjangoFilmStream.git
cd DjangoFilmStream 
```

## 2. Create and activate virtual environment (recommended)
```
python3 -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# .venv\Scripts\activate   # For Windows (PowerShell)
# Or set in in the ID that are u using
```

## 3. Install dependencies
```
pip install -r DjangoFilmStream/requirements.txt
```

## 4. 🔧 Instalación de PostgreSQL (Linux, macOS y Windows)
En Ubuntu/Debian
```
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

En macOS con Homebrew
```
brew install postgresql
brew services start postgresql
```

En Windows
Descarga desde https://www.postgresql.org/download/windows/
Sigue el instalador gráfico (recomendado incluir pgAdmin).

## 5. Create the Databse ans user (PostgreSQL)
Once PostgreSQL is installed and running, follow these steps to create your database:

* Open the PostgreSQL prompt:
```
sudo -u postgres psql
```

* Then run the following SQL commands inside the prompt:
```
-- Create the user (if not already created)
CREATE USER your_username WITH PASSWORD 'your_password';

-- Create the database
CREATE DATABASE <db_name> OWNER your_username;

-- Grant all privileges
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO your_username;

-- Exit psql
\q

```

## 6. Create a .env file in DjangoFilmStream/ and set it there :
> 🔐 The `.env` file contains sensitive database credentials and is not included in version control.
> Request access to the project lead or retrieve it from the secure team drive.


## 7. Run migrations
```
cd DjangoFilmStream
python manage.py migrate
```
