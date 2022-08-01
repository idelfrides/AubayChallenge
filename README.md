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

### 9 | To test question 29 run app by calling curl with  X_VALUE AND Y_VALUE as url parameter, like this

     curl "http://localhost:7200/aubay_question29/X_VALUE/Y_VALUE"

     Example:
          curl "http://localhost:7200/aubay_question29/1/1"      --> True
          curl "http://localhost:7200/aubay_question29/1/100"    --> True
          curl "http://localhost:7200/aubay_question29/9/1"      --> True
          curl "http://localhost:7200/aubay_question29/1/0"      --> True
          curl "http://localhost:7200/aubay_question29/3/-2"     --> True
          curl "http://localhost:7200/aubay_question29/11/91"    --> False
          curl "http://localhost:7200/aubay_question29/7/70"     --> False


### **NOTE 1** I am not sure about that number. But the problem was ...
### Return 'True' if a sum of x_value and y_value eguals to 1 or if one of them is 1. Return 'False' otherwise.
