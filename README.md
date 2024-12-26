# VendorHub

VendorHub is a Django-based microservices project designed for managing vendor-related operations. The project leverages Docker and Docker Compose for seamless containerized development and deployment.

---

## Prerequisites

Before setting up the project locally, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Samrath49/vendorhub.git
   cd vendorhub
   ```

2. Create and configure the `.env` file:
- Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```

3. Build and start the Docker containers:
    ```bash
   docker-compose up --build
   ```

4. Access the application:
- The Django development server will be available at `http://localhost:8000`.

## Prerequisites

### Running the Project

```bash
docker-compose down
docker-compose up --build
```

### Checking Service Health

```bash
docker-compose exec redis redis-cli ping
docker-compose exec db psql -U postgres
docker-compose exec web python manage.py check
```

### Managing Migrations
- Create and apply migrations for services:

```bash
docker-compose exec web python manage.py makemigrations base
docker-compose exec web python manage.py migrate base

docker-compose exec web python manage.py makemigrations product_service
docker-compose exec web python manage.py makemigrations order_service
docker-compose exec web python manage.py makemigrations payment_service
docker-compose exec web python manage.py makemigrations shipment_service

docker-compose exec web python manage.py migrate
```    

### Deleting the Database
```bash
docker volume rm vendorhub_postgres_data
``` 

### Deleting Migration Files
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
``` 