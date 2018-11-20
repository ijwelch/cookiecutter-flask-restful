# {{cookiecutter.project_name}}

## How to Prepare your Dev Environment

This project uses pipenv  (https://pipenv.readthedocs.io/en/latest/)

### Setup your Pipenv environment.

Pipenv consolidates _virtualenv_ and _pip requirements.txt_ into a single command.  

Create the pipenv file (based on Python 3);

`pipenv --three`  

### Activate your Pipenv

`pipenv shell`

Alternatively you can run a command inside the environment,  without activating a whole shell as follows;

`pipenv run <command>`

### Install Dependencies

`pipenv install`

## How to Deploy

This component is deployed as Docker container.  __Travis__ checks the code out and build the container,  but you can build and test the container as follows;

`docker build -t signature/{{cookiecutter.project_name}} .`