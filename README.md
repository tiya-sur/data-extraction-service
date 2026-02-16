
# Data Extraction Service

A Django REST API for managing asynchronous data extraction jobs.

---

## Setup

### 1. Create Virtual Environment
python -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Setup Environment
Copy .env.example → .env

### 4. Run Migrations
python manage.py migrate

### 5. Run Server
python manage.py runserver

---

## Swagger API Docs

http://127.0.0.1:8000/swagger/

---

## Endpoints

POST   /api/v1/scan/start  
GET    /api/v1/scan/status/<job_id>  
GET    /api/v1/scan/result/<job_id>  
POST   /api/v1/scan/cancel/<job_id>  
DELETE /api/v1/scan/remove/<job_id>  

---

## Run Tests

python manage.py test
