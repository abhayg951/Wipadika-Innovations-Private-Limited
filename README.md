# URL Shortener API

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database in `config.py` and create the `.env` file:**
   - In the `.env` file, create the following environment variables:
     - `DATABASE_NAME`
     - `DATABASE_HOST`
     - `DATABASE_PORT`
     - `DATABASE_USER`
     - `DATABASE_PASSWORD`

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- **POST /shorten:** Accepts a long URL and returns a shortened URL code.
- **GET /{short_code}:** Returns the original URL.
