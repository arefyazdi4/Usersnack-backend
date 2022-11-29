# Usersnack-backend

Tech stacks of this project:

- Django / Django Rest Framework
- Postgres
- Docker
- Swagger

### 1. Download the project:

- `git clone "https://github.com/arefyazdi4/Usersnack-backend.git"`

### 2. Build The Project:

- `docker-compose build`

### 3. Rune the project:

- `docker-compose up ` \ `docker-compose up -d`

### 4. Setting up the project:
- rename usersnack/.env.example to usersnack/.env
- `docker exec -it usersnack sh`
- `python manage.py migrate `
- `python manage.py createadmin `

## 5. Now you can see Browsable Api

- Api to see the endpoint List and Detail -> `127.0.0.1:8000/api/`
- Admin Panel -> `127.0.0.1:8000/admin/`


- ### auto generated documentation:
  - Swagger Documentation -> `127.0.0.1:8000/swagger/`
  - Redoc Documentation -> `127.0.0.1:8000/redoc/`
