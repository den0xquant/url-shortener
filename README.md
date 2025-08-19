# URL Shortener 🔗

A simple, high-performance URL shortener built with **Python 3.13** and **FastAPI**.  
It converts long URLs into short unique links and provides fast redirection.

---

## ✨ Features
- 🔹 Generate short links of fixed length (7 chars)
- 🔹 Redirect users instantly to the original URL
- 🔹 Store mappings in PostgreSQL with caching in Redis
- 🔹 REST API with OpenAPI docs
- 🔹 Ready-to-use Docker setup

---

## 🛠 Tech Stack
- **Backend:** Python 3.13, FastAPI
- **Database:** PostgreSQL
- **Cache:** Redis
- **Other:** Docker, SQLAlchemy, Alembic

---

## 📦 Installation

```bash
git clone https://github.com/username/url-shortener.git
cd url-shortener
```

Create a .env file (see .env.example for reference).

Install dependencies:

```bash
uv sync
```

## ▶️ Usage

Run locally:

```bash
uvicorn app.main:app --reload
```

Run with Docker:

```bash
docker compose watch
```

API Docs available at:
```bash
http://localhost:8000/docs
```

## 📌 API Endpoints

- POST /shorten — create a short URL

    Example request:

    ```json
    { "url": "https://example.com/very/long/link" }
    ```

- GET /{short_code} — redirect to original URL

## 🧩 Project Structure

```bash
url-shortener/
│── app/
│   ├── api/        # endpoints
│   ├── core/       # config & settings
│   ├── models/     # DB models
│   ├── services/   # logic for shortening & redirect
│   └── tests/          # tests
│── docker-compose.yaml
│── README.md
```

## 🧪 Tests

```bash
pytest -v
```

## 📄 License
MIT
