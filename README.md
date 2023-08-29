# Rare Django Server

## Description

This is the server-side API for the Rare Publishing Platform. It is built using Django and the Django REST Framework. This API provides endpoints for user authentication, content management, and other features required by the Rare client application.

## Features

- User authentication with JWT
- CRUD operations for Posts, Comments, Categories, Tags

## Installation

1. Clone this repository and navigate into the directory.
2. Create a virtual environment: `python -m venv rareenv`
3. Activate the virtual environment: 
    - On Windows: `source rareenv/Scripts/activate`
    - On MacOS/Linux: `source rareenv/bin/activate`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Client-Side Code

The client-side code for this project can be found [here](https://github.com/NSS-Day-Cohort-64/rare-django-client-init-to-win-it).

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.


---
