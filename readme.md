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

# 1 - USER

## 1.1 - Get list of Users

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

## 1.2 - Create a new User

### Request

`POST users/signup`

http://localhost:5000/users/signup

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
        "id": 1,
        "user_name": "User 01",
        "user_birthdate": "Sun, 15 Aug 1999 00:00:00 GMT",
        "user_phone": "31901234567",
        "user_city": "Belzonte",
        "is_owner": true,
        "created_at": "Wed, 20 Oct 2021 07:44:07 GMT"
    }

## 1.3 - Login user

### Request

`POST /users/login`

    http://localhost:5000/users/login

     {
         "user_cpf": "01234567890",
         "password": "examplepassword"
     }

### Response

     {
         "access_token":            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.  eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDU2NzUwNSwianRpIjoiZDFkNWUzMzctMzU1MC00OGJhLWEzMjEtMDMwZDEwN2Y3YzgyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MTQsInVzZXJfbmFtZSI6IkFkcnllbGwiLCJ1c2VyX2JpcnRoZGF0ZSI6IlN1biwgMTUgQXVnIDE5OTkgMDA6MDA6MDAgR01UIiwidXNlcl9waG9uZSI6IjAwMDAwMDAwMDAwIiwidXNlcl9jaXR5IjoiQmV0aW0iLCJpc19vd25lciI6dHJ1ZSwiY3JlYXRlZF9hdCI6Ik1vbiwgMTggT2N0IDIwMjEgMTE6MjY6MDUgR01UIn0sIm5iZiI6MTYzNDU2NzUwNSwiZXhwIjoxNjM0NTY4NDA1fQ.ndS_1fJcZuWyfg8o2BGDE2ANf_1NCLb_aXYJxIT8VO8"
     }

## 1.4 - Delete user

### Request

`DELETE /users`

    http://localhost:5000/users

    {
        "id": 1
    }

### Response

     no body returned for response

## 1.5 - update user

### Request

`UPDATE /users`

    http://localhost:5000/users

    {
        "id": 1
    }

### Response

     no body returned for response

# 2 - PETS

## 2.1 - Get list of Pets

### Request

`GET /pets/list`

    http://localhost:5000/pet/list

### Response

    {
        "data": [
            {
            "id": 1,
            "pet_type": "Dogs",
            "pet_race": "Buldogue",
            "pet_size": "Small",
            "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
            "pet_description": "Text with the description",
            "pet_localization": "Rio de Janeiro - RJ",
            "contact_phone": "(00)99999-9999"
            }
        ]

}

## 2.2 - Create a new pet

### Request

`POST /pet/list`

    http://localhost:5000/pet/list

### JSON model

    {
        "pet_type": "Dogs",
        "pet_race": "Buldogue",
        "pet_size": "Small",
        "pet_birthdate": "11/10/2001",
        "pet_description": "Text with the description",
        "pet_localization": "Rio de Janeiro - RJ",
        "contact_phone": "(00)99999-9999"
    }

### Response

    {
        "data": {
            "id": 1,
            "pet_type": "Dogs",
            "pet_race": "Buldogue",
            "pet_size": "Small",
            "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
            "pet_description": "Text with the description",
            "pet_localization": "Rio de Janeiro - RJ",
            "contact_phone": "(00)99999-9999"
        }
    }

## 2.3 - Delete pet

### Request

`DELETE /pet/list`

    http://localhost:5000/pet/list

### JSON model

    {
        "id": 1
    }

### Response

     No body returned for response

## 2.4 - Update pet

### Request

`UPDATE /pet/list`

### It is necessary to use the "id" to update the other data that are optional.

    http://localhost:5000/pet/list

### JSON model

    {
        "id": 1,
        "pet_type": "cat",
        "pet_race": "undefined race",
        "pet_size": "Small",
        "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
        "pet_description": "Text with the description",
        "pet_localization": "Rio de Janeiro - RJ",
        "contact_phone": "(00)12345-6666"
    }

### Response

     No body returned for response

## 2.5 - Select pet

### Request

`POST /pet/list/select-pet`

    http://localhost:5000/pet/list/select-pet

### JSON model

    {
        "id": 1,
    }

### Response

    {
        "data": {
            "id": 1,
            "pet_type": "cat",
            "pet_race": "undefined race",
            "pet_size": "Small",
            "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
            "pet_description": "Text with the description",
            "pet_localization": "Rio de Janeiro - RJ",
            "contact_phone": "(00)12345-6666"
        }

}

# 3 - PETS ADOPTED

## 3.1 - Get list of Pets adopted

### Request

`GET /pets`

    http://localhost:5000/pet

### Response

    {
      "data": [
        {
            "id": 2,
            "pet_name": "king",
            "pet_info": {
            "id": 5,
            "pet_type": "cat",
            "pet_race": "undefined race",
            "pet_size": "Small",
            "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
            "pet_description": "Text with the description",
            "pet_localization": "Rio de Janeiro - RJ",
            "contact_phone": "(00)12345-6666"
        }
      ]
    }

## 3.2 - Create a new adoption

### Request

`POST /pet`

    http://localhost:5000/pet

### JSON model

    {
        "pet_name": "Sansão",
        "pet_id": 1
    }

### Response

    {
        "data": {
            "id": 1,
            "pet_name": "Sansão",
            "pet_info": {
            "id": 1,
            "pet_type": "cat",
            "pet_race": "undefined race",
            "pet_size": "Small",
            "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
            "pet_description": "Text with the description",
            "pet_localization": "Rio de Janeiro - RJ",
            "contact_phone": "(00)12345-6666"
            }
        }
    }

## 2.3 - Delete pet

### Request

`DELETE /pet`

    http://localhost:5000/pet

### JSON model

    {
        "id": 1
    }

### Response

     No body returned for response

## 2.4 - Update pet

### Request

`UPDATE /pet`

### It is necessary to use the "id" to update the other data that are optional.

    http://localhost:5000/pet

### JSON model

    {
        "id": 1,
        "pet_name": "Caramelo",
    }

### Response

     no body returned for response

## 3.5 - Select pet

### Request

`POST /pet/list/select`

    http://localhost:5000/pet/list/select

### JSON model

    {
        "id": 1,
    }

### Response

    {
        "data": {
            "id": 1,
            "pet_name": "Caramelo",
            "pet_info": {
            "id": 1,
            "pet_type": "cat",
            "pet_race": "undefined race",
            "pet_size": "Small",
            "pet_birthdate": "Thu, 11 Oct 2001 00:00:00 GMT",
            "pet_description": "Text with the description",
            "pet_localization": "Rio de Janeiro - RJ",
            "contact_phone": "(00)12345-6666"
            }
        }
    }
