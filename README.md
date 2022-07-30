# AUBAY SA Challenge Project With Flask


This is the thecnical challenge for join AUBAY SA  company as Python developer.

## Language/tools Requirements

**Python 3.8.x**

**Flask newest version**

**pip newest version**


## STEPS TO RUN THIS APP ON YOUR MACHINE

### 1 | Clone the remote repository to start testing

     git clone https://github.com/idelfrides/AubayChallenge.git


### 2 | Create your virtualenv like

     virtualenv [your_venv_name]

### 3 | Virtualenv activation

     source [your_venv_name]/bin/activate

If you are using fish, write

     source [your_venv_name]/bin/activate.fish


### 4 | Update pip to newest version

     pip install -U pip

### 5 | Install requirements

     pip install -r requirements.txt

### 6 | To Set up project fully, first you gonna need to run flask server, like this

     python flask_app.py  or  python flask_app.py runserver


### 7 | Run app by calling curl with CASH_VALUE as url parameter, like this

     curl "http://localhost:7200/runapp_with_cash/CASH_VALUE"

     Example:
          curl "http://localhost:7200/runapp_with_cash/42"


### 8 | Run app by calling curl with ROUND_NUMBER as url parameter, like this

     curl "http://localhost:7200/aubay_runapp_round/ROUND_NUMBER"

     Example:
          curl "http://localhost:7200/aubay_runapp_round/10"

     This endpint will random cash value between 1 and 10000.
