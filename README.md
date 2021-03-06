<p align="center">
    <img height="128" src="https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png">
</p>


## Circle Ci 
[![CircleCI](https://circleci.com/gh/Madscientiste/OpenClassrooms_P13/tree/master.svg?style=svg)](https://circleci.com/gh/Madscientiste/OpenClassrooms_P13/tree/master)

## Local Development

### Requirements
- [Python 3.9+](https://www.python.org/downloads/) 
- [GIT](https://git-scm.com/downloads)

### Setup

Clone this repository to your local machine & cd into it.

```bash
git clone <repo_url> <destination>
cd <destination>
```

Create a virtual environment and activate it.

```bash
python -m venv .venv

[windows]
./.venv/Scripts/activate

[UNIX]
source .venv/bin/activate
```

Install required dependencies.

```bash
pip install -r requirements.txt
```

when everything has installed correctly, ensure to sync the database schema with the migrations.

> ### if this is the first run from the previous version, fake the inital migrations.

```bash
python manage.py migrate lettings 0001 --fake
python manage.py migrate profiles 0001 --fake
```

Then, migrate 
```bash
python manage.py migrate
``` 

Check everything works correctly

```bash
python -m pytest
```

5 tests should pass.

### Running the Project

```bash
python manage.py runserver
```

#### Check the linting of the project

```bash
python -m flake8
``` 


#### Admin panele can be accessed at http://localhost:8000/admin/
- You can authenticate with `admin` as the username, and `Abc1234!` as the password.

## Deployment

### Accounts Required
- [Circle CI](https://circleci.com)
- [Heroku](https://heroku.com)
- [Docker](https://www.docker.com)
- [Sentry](https://sentry.io)

#### How it Works

```mermaid
graph TD
    A(< branch > get updated)
    A --> D(its the master branch)
    D --> E(Run tests & check linting)
    E --> F(Deploy the newly built image to docker hub)
    E --> G(Deploy to heroku)    
    A --> B(its NOT the master branch)
    B --> T(Run tests & check linting)
```

### Setup CircleCI

Fews environment variables are required to be set inside the CircleCI project.

```bash
DOCKER_IMG = "<docker_username>/<docker_repository>"
# eg: DOCKER_IMG = "shaade/ocr-p13"

DOCKER_PASS = "<docker_password>"
# eg: DOCKER_PASS = your password or access token

DOCKER_USERNAME = "<docker_username>"
# eg: DOCKER_USERNAME = your username
```

### Setup Sentry

Create a new project in Sentry. And save the DSN in the .env variable as `SENTRY_DSN`.

### Setup Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Madscientiste/OpenClassrooms_P13/tree/master)

When the project is deployed to heroku, set the environment variable `SENTRY_DSN` in the project settings, and then reboot all dynos.

```bash	
SENTRY_DSN = "<sentry_dsn>"
# eg: SENTRY_DSN = "https://kqzhrglierzhqglerqughlihuget.ingest.sentry.io/5843684"
```

## Using Docker

You can run the app locally using the following command:

```bash
docker run -p 5000:5000 -e PORT=5000 --env-file ./.env njustn/orc-p13:c361ea0e2639571285ea77bd6d81cf00de63690a