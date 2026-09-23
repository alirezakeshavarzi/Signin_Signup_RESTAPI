# Django REST API Authentication

A backend REST API for user registration and authentication built with **Django** and **Django REST Framework (DRF)**.

This project demonstrates common backend authentication concepts, including a custom Django user model, password hashing, JWT-based authentication, protected API endpoints, and request data validation using DRF serializers.

## Features

* User registration
* Custom `User` model based on Django's `AbstractUser`
* Password hashing using Django's authentication system
* JWT authentication
* Access and Refresh tokens
* Protected API endpoints using `IsAuthenticated`
* User information endpoint for authenticated users
* Request data validation with DRF serializers
* Access to the authenticated user through `request.user`
* Django Admin integration for managing users

## Technologies

* **Python**
* **Django**
* **Django REST Framework**
* **djangorestframework-simplejwt**
* **SQLite**

## Project Structure

```text
project/
│
├── rest_sign_in_out/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
│
├── sign_in_out/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <project-directory>
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Apply the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

| Method | Endpoint              | Authentication | Description                                  |
| ------ | --------------------- | -------------- | -------------------------------------------- |
| POST   | `/register/`          | Not required   | Register a new user                          |
| POST   | `/api/token/`         | Not required   | Obtain access and refresh tokens             |
| POST   | `/api/token/refresh/` | Not required   | Obtain a new access token                    |
| GET    | `/myinfo/`            | Required       | Get information about the authenticated user |

## 1. User Registration

Create a new user by sending a `POST` request to:

```text
/register/
```

### Request

```json
{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
}
```

### Response

```text
"saved!"
```

The password is stored using Django's password hashing mechanism rather than being saved as plain text.

## 2. Obtain JWT Tokens

After registering, obtain an access token and refresh token using:

```text
POST /api/token/
```

### Request

```json
{
    "username": "john",
    "password": "password123"
}
```

### Response

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

The access token is used to authenticate requests to protected endpoints.

## 3. Access Protected User Information

The `/myinfo/` endpoint requires authentication.

```text
GET /myinfo/
```

Include the access token in the `Authorization` header:

```http
Authorization: Bearer <access_token>
```

### Response

```json
{
    "username": "john",
    "email": "john@example.com"
}
```

The authenticated user is accessed through Django REST Framework's:

```python
request.user
```

## 4. Refresh an Access Token

When the access token expires, a new access token can be obtained using the refresh token:

```text
POST /api/token/refresh/
```

### Request

```json
{
    "refresh": "<refresh_token>"
}
```

### Response

```json
{
    "access": "<new_access_token>"
}
```

## Authentication Flow

The authentication flow is:

```text
Register
   │
   ▼
Username + Password
   │
   ▼
POST /api/token/
   │
   ▼
Access Token + Refresh Token
   │
   ├── Access Token ──► Protected API (/myinfo/)
   │
   └── Refresh Token ─► New Access Token
```

Protected endpoints use DRF's `IsAuthenticated` permission class to ensure that only authenticated users can access them.

## Custom User Model

The project uses a custom user model based on Django's `AbstractUser`.

The current custom field is:

```python
phone = models.IntegerField(null=True)
```

The user model also retains Django's standard user fields such as:

* `username`
* `first_name`
* `last_name`
* `email`
* `password`

## Django Admin

The custom `User` model is registered in Django Admin, allowing user information to be viewed and managed through the admin interface.

The admin interface is available at:

```text
/admin/
```

## Notes

This project is primarily an educational backend project focused on understanding:

* Django's authentication system
* Custom user models
* Django REST Framework
* Serializers
* Protected API endpoints
* JWT authentication
* Access and refresh token workflows
* Basic REST API design
