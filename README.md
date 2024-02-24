# Microblog Flask Application

This Flask application is a simple microblogging platform where users can post short messages. It is built using Flask and SQLAlchemy.

## Features

- User authentication and registration.
- Posting messages.
- User profiles and avatars.
- Password reset functionality.

## Installation

Clone the repository:

```
git clone https://github.com/saitoi/microblog-flask.git
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Configuration

The application is configured through the `config.py` file. Key configurations include:

- `SECRET_KEY`: A secret key used for securing cookies.
- `SQLALCHEMY_DATABASE_URI`: The database URI that should be used for the connection. The application uses SQLite as its database, with the database file (`app.db`) located at the root of the project directory.
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD`: Configuration for the email server used to send password reset emails.
- `ADMINS`: A list of the email addresses of the administrators.

## Running the Application

To run the application:

```
flask run
```

## User Authentication

The application supports user registration and login. User passwords are hashed for security.

## Password Reset

If a user forgets their password, they can request a password reset email. This email contains a secure token allowing them to reset their password without needing to contact an administrator.

## Database

The application uses SQLite, a lightweight disk-based database, for storing user and post data. SQLAlchemy ORM is used for database interactions.

## Contributions

Contributions to this project are welcome. Please fork the repository and submit a pull request.
