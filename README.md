# 📚 Library Service API

A modern library management system built with Django REST Framework. This service allows for managing a book catalog, tracking borrowings, and receiving real-time administrative notifications via Telegram.

## 🚀 Key Features

* **User Service**: Registration and authentication using JWT (JSON Web Tokens).
* **Book Service**: Full CRUD for books including inventory tracking, daily fee calculation, and cover types (Hard/Soft).
* **Borrowing Service**: 
    * Logic for borrowing books with automatic inventory reduction.
    * Filtering by user and active status (is_active).
    * Validation to prevent borrowing out-of-stock books.
* **Return Logic**: A custom endpoint to handle book returns and restore inventory.
* **Notifications**: Integrated Telegram Bot API to notify admins about new borrowings.
* **Documentation**: Interactive API documentation via Swagger and Redoc.
* **Dockerized**: Fully containerized environment for easy setup and deployment.

## 🛠 Tech Stack

- **Python 3.12+**
- **Django & Django REST Framework**
- **PostgreSQL**
- **JWT Authentication** (SimpleJWT)
- **Telegram Bot API**
- **Docker & Docker Compose**
- **drf-spectacular** (OpenAPI 3.0)

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Garichka/library-service-api.git
cd library-service-api
