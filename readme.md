# Pet API

This is an API to deal with the pet adoption process. It let you register as a user, register an pet for adoption and see all the pets already registered.

The entire application is contained within the `app/` directory.

`migrations/` is the version control of the database.

`.env.example` is an example of how application expects `.env` file to be.

`Procfile` is the heroku dyno config file required to run the application on it.

### Install virtual environment

    python -m venv venv

### Activate it

    source venv/bin/activate

### Run app

    flask run -h localhost -p 5000

# REST API

The REST API to the app is described below.
##
Base URL: `url do heroku aqui`

## Get list of Users

### Request

`GET /users`

    http://localhost:5000/users

### Response

    {
        "data": [
            {
                "birthdate": "Sun, 15 Aug 1999 00:00:00 GMT",
                "id": 1,
                "name": "User 01"
            },
            {
                "birthdate": "Sun, 22 Aug 1999 00:00:00 GMT",
                "id": 2,
                "name": "User 02"
            }
        ]
    }

## Create a new User

### Request

`POST /signup`

     http://localhost:5000/signup

JSON model

    {
        "user_name": "User 01",
        "user_birthdate": "1999/08/15",
        "user_cpf": "01234567890",
        "user_city": "Belzonte",
        "user_phone": "31901234567",
        "password": "examplepassword"
    }
    

### Response

    {
        "id": 17,
        "user_birthdate": "Sun, 15 Aug 1999 00:00:00 GMT",
        "user_city": "Betim",
        "user_name": "User 01",
        "user_phone": "00000000000"
    }


## Login

### Request

`POST /login`

     {
         "user_cpf": "01234567890",
         "password": "passwordexample"
     }

### Response

     {
         "access_token":            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.  eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDU2NzUwNSwianRpIjoiZDFkNWUzMzctMzU1MC00OGJhLWEzMjEtMDMwZDEwN2Y3YzgyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MTQsInVzZXJfbmFtZSI6IkFkcnllbGwiLCJ1c2VyX2JpcnRoZGF0ZSI6IlN1biwgMTUgQXVnIDE5OTkgMDA6MDA6MDAgR01UIiwidXNlcl9waG9uZSI6IjAwMDAwMDAwMDAwIiwidXNlcl9jaXR5IjoiQmV0aW0iLCJpc19vd25lciI6dHJ1ZSwiY3JlYXRlZF9hdCI6Ik1vbiwgMTggT2N0IDIwMjEgMTE6MjY6MDUgR01UIn0sIm5iZiI6MTYzNDU2NzUwNSwiZXhwIjoxNjM0NTY4NDA1fQ.ndS_1fJcZuWyfg8o2BGDE2ANf_1NCLb_aXYJxIT8VO8"
     }