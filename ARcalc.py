#!/usr/bin/python
# -*- coding: utf-8 -*-
# Written by @lapiswoof
# Inspired by other genshin AR calulators because they made you modify the code variables to get your data. I said screw that and made it all input based.
# No need to modify the code 

CurrentAR = int(input('What is your current AR? '))
CurrentEXP = int(input('How much exp do you have? '))
FutureAR = int(input('What AR do you want? '))

resinUSE = int(input('How much resin do you use a day? '))
resinEXPper20 = 100
resinPerDay = resinUSE / 20 * resinEXPper20

dailyCommEXP1 = 500 + (4 * 175)
dailyCommEXP2 = 500 + (4 * 200)
dailyCommEXP3 = 500 + (4 * 225)
dailyCommEXP4 = 500 + (4 * 250)

exp_table = {
    1: 0,
    2: 375,
    3: 875,
    4: 1500,
    5: 2225,
    6: 3075,
    7: 4025,
    8: 5100,
    9: 6300,
    10: 7600,
    11: 9025,
    12: 10550,
    13: 12200,
    14: 13975,
    15: 15850,
    16: 17850,
    17: 20225,
    18: 22725,
    19: 25350,
    20: 28125,
    21: 30950,
    22: 34375,
    23: 38100,
    24: 42100,
    25: 46400,
    26: 50975,
    27: 55850,
    28: 61000,
    29: 66450,
    30: 72175,
    31: 78200,
    32: 84500,
    33: 91100,
    34: 98000,
    35: 105175,
    36: 112650,
    37: 120400,
    38: 128450,
    39: 136775,
    40: 145400,
    41: 155950,
    42: 167475,
    43: 179950,
    44: 193400,
    45: 207800,
    46: 223150,
    47: 239475,
    48: 256750,
    49: 275000,
    50: 294200,
    51: 320600,
    52: 349400,
    53: 380600,
    54: 414200,
    55: 450200,
    56: 682550,
    57: 941500,
    58: 1227250,
    59: 1540075,
    60: 1880200,
    }


def main():
    def calc1():
        print('Total EXP Required: ', totalExp)
        print('Days til AR Goal: ', round(totalExp /exp1,2), "days!")
        exit()
    def calc2():
        print('Total EXP Required: ', totalExp)
        print('Days til AR Goal: ', round(totalExp /exp2,2), "days!")
        exit()
    def calc3():
        print('Total EXP Required: ', totalExp)
        print('Days til AR Goal: ', round(totalExp /exp3,2), "days!")
        exit()
    def calc4():
        print('Total EXP Required: ', totalExp)
        print('Days til AR Goal: ', round(totalExp /exp4,2), "days!")
        exit()
    def yeah():
        print("You can't go higher then AR 60")
        exit()
    if CurrentAR < 12:
        print('Daily quests do not start until ar 12.')
        exit()
    else:
        if CurrentAR in range(12, 16):
            totalExp = exp_table[FutureAR] - exp_table[CurrentAR] - CurrentEXP
            exp1 = dailyCommEXP1 + resinPerDay
            calc1()
        else:
            if CurrentAR in range(16, 26):
                totalExp = exp_table[FutureAR] - exp_table[CurrentAR] - CurrentEXP
                exp2 = dailyCommEXP2 + resinPerDay
                calc2()
            else:
                if CurrentAR in range(26, 36):
                    totalExp = exp_table[FutureAR] - exp_table[CurrentAR] - CurrentEXP
                    exp3 = dailyCommEXP3 + resinPerDay
                    calc3()
                else:
                    if CurrentAR in range(36, 61):
                        totalExp = exp_table[FutureAR] - exp_table[CurrentAR] - CurrentEXP
                        exp4 = dailyCommEXP4 + resinPerDay
                        calc4()
                    else:
                        yeah()

main()