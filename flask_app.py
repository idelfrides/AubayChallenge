#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Pyton importatinons
from random import randint
from threading import TIMEOUT_MAX
import time

from flask_app import __app__
from flask import request


from AubayLib import (
    change, AubayChallenge, make_reponse, question29
)
#-------------------------------------------------------------------------
#                  RUN APP FUNCTION BEGIN HERE
#-------------------------------------------------------------------------


@__app__.route('/home')
@__app__.route('/inicio')
@__app__.route('/index')
@__app__.route('/')
def hello():
    APP_INFO = '''

    This is a AUBAY SA thecnical challenge for joing that company as a python developer. This is answer for question number 30.

    '''

    return APP_INFO


@__app__.route('/aubay_question29/<x_value>/<y_value>')
def solving_question_29(x_value, y_value):

    status_  = question29(int(x_value), int(y_value))

    response_ = f'aubay_question29 | RESULT: {status_}'

    return make_reponse(response_)


@__app__.route('/aubay_runapp_round/<totalround_>')
def aubay_runapp_round(totalround_):

    start_time_ = time.time()

    AubayChallenge()

    total_rounds = int(totalround_)

    round_ = 1

    while True:

        print(f'\n\n\t\t ROUND --> [ {round_} ]\n')

        CASH = randint(1, 10000)

        print(f'\n\n\t\t CASH IS --> [ {CASH} ]\n\n')

        response_ = change(cash=CASH)

        if not response_:
            response_ = 'VALUE NOT ALLAWED'

        print('\n\n')
        print('#'*100)
        print('\n\t\t FINAL RESULT')
        print(f'\n\n\t\t {response_}')
        print('\n')
        print('#'*100)

        time.sleep(5)

        round_ += 1

        if round_ > total_rounds:
            break

    stop_time = time.time()
    total_round_time = stop_time - start_time_

    total_round_time /= 60

    total_minutes = str(total_round_time).split('.')[0]
    total_seconds = str(total_round_time).split('.')[1]

    show_info_time = 'TOTAL TIME: %.0f min e %.0f milissegundos' % (int(total_minutes), int(total_seconds))

    endpoint = 'aubay_runapp_round | {}'.format(show_info_time)

    return make_reponse(endpoint)



@__app__.route('/runapp_with_cash/<cash_value>')
def runapp_with_cash(cash_value):

    start_time_ = time.time()

    AubayChallenge()

    CASH = int(cash_value)

    print(f'\n\n\t\t CASH IS --> [ {CASH} ]\n\n')

    response_ = change(cash=CASH)

    if not response_:
        response_ = 'VALUE NOT ALLAWED'

    time.sleep(20)


    print('\n\n')
    print('#'*100)
    print('\n\t\t FINAL RESULT')
    print(f'\n\n\t\t {response_}')
    print('\n')
    print('#'*100)

    stop_time = time.time()
    total_round_time = stop_time - start_time_

    total_round_time /= 60

    total_minutes = str(total_round_time).split('.')[0]
    total_seconds = str(total_round_time).split('.')[1]

    show_info_time = 'TOTAL TIME: %.0f min e %.0f milissegundos' % (int(total_minutes), int(total_seconds))

    endpoint = 'runapp_with_cash | {}'.format(show_info_time)

    return make_reponse(endpoint)



# -----------------------------------------------------------------------------


if __name__ == '__main__':

    __app__.run(
        __app__.config['FLASK_HOST'], port=__app__.config['FLASK_PORT']
    )
