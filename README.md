# Epic-Event


Epic-Event and a REST API that allows you to set up collaboration between teams for the follow-up of customers, current contracts and events. The teams are managers and salespeople, each status gives privilege (see Postman documentation)

## Installation

This locally-executable API can be installed and executed from [http://localhost:8000/](http://localhost:8000/) using the following steps.

### Option 1: Installation and execution with pipenv

For this method, it is necessary to have pipenv already installed on your python installation. If pipenv is not already installed on your computer, refer to [this page](docs/pipenv/installation-en.md).

1. Clone this repository using `$ git clone https://github.com/mlsc63/Epic-Event.git`
2. Move to the softdesk root folder with `$ cd Epic-Event`
3. Install project dependencies with `pipenv install` 
4. Edit the setting.py file with your PostgreSQL username
5. Run the server with `pipenv run python manage.py runserver`

When the server is running after step 5 of the procedure, the Epic-Event API can
be requested from endpoints starting with the following base URL: [http://localhost:8000/](http://localhost:8000/).

Steps 1-4 are only required for initial installation. For subsequent launches
of the API, you only have to execute step 5 from the root folder of the project.

### Option 2: Installation and execution without pipenv (using venv and pip)

1. Clone this repository using `$git clone https://github.com/mlsc63/SoftDesk.git`
2. Move to the ocmovies-api root folder with `$ cd SoftDesk`
3. Create a virtual environment for the project with `$ py -m venv env` on windows or `$ python3 -m venv env` on macos or linux.
4. Activate the virtual environment with `$ env\Scripts\activate` on windows or `$ source env/bin/activate` on macos or linux.
5. Install project dependencies with `$ pip install -r requirements.txt`
6. Edit the setting.py file with your PostgreSQL username`
7. Run the server with `$ python manage.py runserver`

### Documentation Postman
https://documenter.getpostman.com/view/14859712/UUxzBTX5
