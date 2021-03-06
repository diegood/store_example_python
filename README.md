# minimart

Minimart Is a stock control to Coco brand 

## Quick Start

Run the application:

    make run

And open it in the browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Prerequisites

This is built to be used with Python 3. Update `Makefile` to switch to Python 2 if needed.

Some Flask dependencies are compiled during installation, so `gcc` and Python header files need to be present.
For example, on Ubuntu:

    apt install build-essential python3-dev


## Development environment and release process

 - create virtualenv with Flask and minimart installed into it (latter is installed in
   [develop mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode) which allows
   modifying source code directly without a need to re-install the app): `make venv`

 - run development server in debug mode: `make run`; Flask will restart if source code is modified

 - run tests: `make test` (see also: [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/))

 - run on debug mode `make dev`

 - to remove virtualenv and built distributions: `make clean`

 - to add more python dependencies: add to `install_requires` in `setup.py`

 - to modify configuration in development environment: edit file `settings.cfg`; this is a local configuration file
   and it is *ignored* by Git - make sure to put a proper configuration file to a production environment when
   deploying


## Deployment
 TODO

## Guides I used or tools
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
  - [cookiecutter base flask](https://github.com/candidtim/cookiecutter-flask-minimal.git)
- [dev.to](https://dev.to/nahidsaikat/flask-with-sqlalchemy-marshmallow-5aj2).
- [sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/master/quickstart/#a-minimal-application)
- [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [flask restx](https://flask-restx.readthedocs.io/en/latest/)