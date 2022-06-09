<p align="center">
    <img height="128" src="https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png">
</p>

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

### Requirements
- [Circle CI Account](https://circleci.com)
- [Heroku Account](https://heroku.com)
- [Docker Account](https://www.docker.com)


### Usefull Commands
```bash
# Docker
docker login -u <username>
> password: <access_token or password>

docker build -t <image_name> .
docker push <image_name>
docker run -p 5000:5000 -e PORT=5000 <image_name>

# Heroku
heroku login
heroku container:login
heroku container:push web
heroku container:release web
```