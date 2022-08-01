#!usr/bin/env python 3
# -*- coding: utf-8 -*-

from random import randint
import time


def AubayChallenge():
    """
    # AUBAY SA app info
    ---
    #### This is a AUBAY SA thecnical challenge for joing that company as a python developer'
    """
    print('\n\n This is a AUBAY SA thecnical challenge for joing that company as a python developer')

    return


def change(cash):

    """
    # Question 30
    ## This a solution for question number 30

    """

    if not (0 < cash < 100000):
        print(f'CASH OUT OF RANGE: COME IN CASH {cash}.\n\n APP WILL BE QUITED!')
        time.sleep(40)
        return


    if cash < 2:
        return None

    two, five, ten = start_bill_qtd()

    if (cash % 2 == 0) and (cash % 5 == 0) and (cash % 10 == 0):
        two, five, ten = rest_division_zero(cash=cash)
    else:
        two, five, ten = rest_division_notzero(cash=cash)


    response_ =  {
        'two': two,
        'five': five,
        'ten': ten,
    }

    return response_


def question29(x_value, y_value):

    """
    # Question 29
    ---
    #### This a solution for question number 29. I am not sure about that number. But the problem was ...

    #### Return 'True' if a sum of x_value and y_value eguals to 1 or if one of them is 1. Return 'False' otherwise.

    """

    status_ = False

    if (x_value + y_value) == 1:
        status_ = True
    elif x_value == 1 or y_value == 1:
        status_ = True
    else:
        pass

    return status_



def start_bill_qtd():
    return 0, 0, 0


def rest_division_zero(cash):
    """
    # Rest of division zero
    #### Build logic for this app when rest of division is zero for all
    """

    hold_bill_qtd = []
    hold_bill_qtd_type = {}

    if cash % 2 == 0:
        two = cash // 2
        hold_bill_qtd_type[two] = 'two'
        hold_bill_qtd.append(two)

    if cash % 5 == 0:
        five = cash // 5
        hold_bill_qtd_type[five] = 'five'
        hold_bill_qtd.append(five)

    if cash % 10 == 0:
        ten = cash // 10
        hold_bill_qtd_type[ten] = 'ten'
        hold_bill_qtd.append(ten)


    for bill_qtd in hold_bill_qtd:
        if bill_qtd == 0:
            hold_bill_qtd.remove(bill_qtd)

    hold_bill_qtd.sort()

    min_bill = hold_bill_qtd[0]

    bill_type = hold_bill_qtd_type[min_bill]

    if bill_type == 'two':
        two = min_bill
        _, five, ten = start_bill_qtd()

    if bill_type == 'five':
        five = min_bill
        two, _, ten = start_bill_qtd()

    if bill_type == 'ten':
        ten = min_bill
        two, five, _ = start_bill_qtd()

    return two, five, ten


def get_float_division(cash):

    fd_2 = cash / 2
    fd_5 = cash / 5
    fd_10 = cash / 10

    return fd_2, fd_5, fd_10


def rest_division_notzero(cash):
    """
    # Rest of division not zero
    #### Build logic for this app when rest of division is  not zero for all
    """

    hold_bill_qtd_type = {
        'two': 0,
        'five': 0,
        'ten': 0
    }

    two, five, ten = get_float_division(cash=cash)

    min_bill_key, min_bill = get_bill_key_value(two, five, ten, oper='min')

    real_min_bill = int(str(min_bill).split('.')[0])
    result_rest = int(str(min_bill).split('.')[1])
    hold_bill_qtd_type[min_bill_key] = real_min_bill  # update


    while True:

        print('*'*80)
        print('\n\t CURRENT STATUS OF RESULT')
        print(f'\n\t {hold_bill_qtd_type}\n ')
        print('*'*80)
        time.sleep(3)

        fd_2, fd_5, fd_10 = get_float_division(cash=result_rest)

        bills_values_type = {fd_2: 'two', fd_5: 'five', fd_10: 'ten'}

        bills_values = list(bills_values_type.keys())

        index_ = 0
        while True:
            b_value = bills_values[index_]

            if b_value < 1:
                print(f'\n VALUE WILL BE REMOVED. IT IS < 1 : {b_value} \n')
                bills_values.remove(b_value)
                index_ = 0
            else:
                index_ += 1

            if index_ >= len(bills_values):
                break

        bills_values.sort()
        try:
            min_bill = bills_values[0]
        except (IndexError, ValueError, TypeError):
            break

        rest_min_bill_key = bills_values_type[min_bill]  # get type:two or five or ten

        min_bill_help = min_bill
        min_bill = int(str(min_bill).split('.')[0])

        result_rest_percent = round((min_bill_help - min_bill), 2)

        if rest_min_bill_key == 'two':
            two = min_bill
            hold_bill_qtd_type['two'] = two  # update Two
            result_rest = result_rest_percent * 2

        if rest_min_bill_key == 'five':
            five = min_bill
            hold_bill_qtd_type['five'] = five  # update five
            result_rest = result_rest_percent * 5

        if rest_min_bill_key == 'ten':
            ten = min_bill
            hold_bill_qtd_type['ten'] = ten  # update ten
            result_rest = result_rest_percent * 10


        if result_rest == 0:
            break


    return hold_bill_qtd_type['two'], hold_bill_qtd_type['five'], hold_bill_qtd_type['ten']


def get_bill_key_value(value_bill_two, value_bill_five, value_bill_ten, oper='min'):

    hold_bill_qtd_type = {}

    if oper == 'min':

        hold_bill_qtd_type['two'] = value_bill_two
        hold_bill_qtd_type['five'] = value_bill_five
        hold_bill_qtd_type['ten'] = value_bill_ten

        bill_keys = list(hold_bill_qtd_type.keys())
        bill_values = list(hold_bill_qtd_type.values())

        help_bill_values_ = bill_values.copy()

        bill_values.sort()             # smallest to largest

        bill = bill_values[0]

        bill_posi = help_bill_values_.index(bill)

        bill_key = bill_keys[bill_posi]

    if oper == 'max':

        hold_bill_qtd_type['two'] = value_bill_two
        hold_bill_qtd_type['five'] = value_bill_five
        hold_bill_qtd_type['ten'] = value_bill_ten

        bill_keys = list(hold_bill_qtd_type.keys())
        bill_values = list(hold_bill_qtd_type.values())

        help_bill_values_ = bill_values.copy()

        bill_values.sort(reverse=True)    # largest to smallest

        bill = bill_values[0]

        bill_posi = help_bill_values_.index(bill)

        bill_key = bill_keys[bill_posi]


    return bill_key, bill


def make_reponse(endpoint):

    ij_jsonify = {
        'state': 'SUCCESS',
        'status': 200,
        'function': '{}'.format(str(endpoint))
    }

    return ij_jsonify
